"""
This procedure will test the neostore functionality.
"""

import os
import unittest
import uuid

import sys
"""
(pp, cd) = os.path.split(os.getcwd())
sys.path.append(pp)
print("Append {pp} to path, is now {lp}".format(pp=pp, lp=sys.path))
"""

print("Before import create_app")
from competition import create_app
print("Before import neostore")
from competition import neostore
print("Before import models_graph")
# from competition import models_graph as mg
from datetime import date

# Import py2neo to test on class types
from py2neo import Node

# @unittest.skip("Focus on Coverage")
class TestNeoStore(unittest.TestCase):

    def setUp(self):
        # Initialize Environment
        print("Create app")
        self.app = create_app('testing')
        self.app_ctx = self.app.app_context()
        print("Push app context")
        self.app_ctx.push()
        print("Set Environment")
        os.environ['Neo4J_User'] = self.app.config.get('NEO4J_USER')
        os.environ['Neo4J_Pwd'] = self.app.config.get('NEO4J_PWD')
        os.environ['Neo4J_Db'] = self.app.config.get('NEO4J_DB')

        print("Get Neo4J User environment")
        neo4j_params = dict(
            user=os.environ.get('Neo4J_User'),
            password=os.environ.get('Neo4J_Pwd'),
            db=os.environ.get('Neo4J_Db')
        )
        print("Get NS")
        # self.ns = models_graph.ns()
        self.ns = neostore.NeoStore(**neo4j_params)
        self.ns.init_graph()
#       my_env.init_loghandler(__name__, "c:\\temp\\log", "warning")

    def tearDown(self):
        self.app_ctx.pop()

    def test_date(self):
        # This function tests the date_node method, remove_date and the clear_date_node method.
        nr_nodes = len(self.ns.get_nodes())
        # Set Dates
        dsd = date(year=1963, month=7, day=2)
        self.ns.date_node(dsd)
        dsc = date(year=1964, month=10, day=28)
        self.ns.date_node(dsc)
        # Number of nodes +3: Year - Month - Day
        ds_nr_nodes = len(self.ns.get_nodes())
        self.assertEqual(nr_nodes+6, ds_nr_nodes)
        # Test to set date from string
        self.assertTrue(isinstance(self.ns.date_node("1963-07-02"), Node))
        # Test date from invalid string is False
        self.assertFalse(isinstance(self.ns.date_node("OngeldigeDatum"), Node))
        self.ns.clear_date()
        # Check number of nodes back to original number
        ds_nr_nodes = len(self.ns.get_nodes())
        self.assertEqual(nr_nodes, ds_nr_nodes)

    def test_remove_relation(self):
        # First create 2 nodes and a relation
        label = "TestNode"
        node1_params = dict(
            testname="Node1"
        )
        node1_node = self.ns.create_node(label, **node1_params)
        node2_params = dict(
            testname="Node2"
        )
        node2_node = self.ns.create_node(label, **node2_params)
        rel = "TestRel"
        self.ns.create_relation(from_node=node1_node, rel=rel, to_node=node2_node)
        # Then remove the relation
        self.ns.remove_relation_node(start_node=node1_node, end_node=node2_node, rel_type=rel)
        self.ns.remove_node_force(node1_node["nid"])
        self.ns.remove_node_force(node2_node["nid"])


if __name__ == "__main__":
    unittest.main()
