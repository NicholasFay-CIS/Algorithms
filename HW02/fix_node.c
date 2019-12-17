//
// Created by Nicholas David Fay on 5/27/19.
//
#include "heads/Tree.h"

BST::BST()
{
    // Inits the Binary Search Tree's source node "root" to Null
    source_node = nullptr;
}

struct tileNode*BST::optimizeInsert(tileNode *node, int nodeID, Tile *tile)
{
    if(node == nullptr) {
        node = new struct tileNode;
        node->nodeID = nodeID;
        node->leftchild = nullptr;
        node->rightchild = nullptr;
        node->tile = tile;
    }
    else if(nodeID < node->nodeID) {
        struct tileNode *left_node;
        left_node = optimizeInsert(node->leftchild, nodeID, tile);
        node->leftchild = left_node;
        left_node->parent = node;
        left_node->tile = tile;
    }
    else if(nodeID > node->nodeID) {
        struct tileNode *right_node;
        right_node = optimizeInsert(node->rightchild, nodeID, tile);
        node->rightchild = right_node;
        right_node->parent = node;
        right_node->tile = tile;
    }
    return node;
}

void BST::insert(tileNode *tileNode, int nodeID, string name)
{
    // if the inserted tile is less than the new tile
    if(nodeID < tileNode->nodeID){
        // checks to see if the left child is NULL
        if(tileNode->leftchild != nullptr){
            // Recurse
            insert(tileNode->leftchild, nodeID, name);
        }else{
            // place the node it is a leaf node
            tileNode->leftchild = new struct tileNode;
            tileNode->leftchild->nodeID = nodeID;
            // set the children to be None
            tileNode->leftchild->leftchild = nullptr;
            tileNode->leftchild->rightchild = nullptr;
            tileNode->name = name;
        }
        // else if the node is is less than the nodeID
    }else if(nodeID >= tileNode->nodeID){
        if(tileNode->rightchild != nullptr){
            // Recurse
            insert(tileNode->rightchild, nodeID, name);
        }else{
            // place the node if it is a leaf
            tileNode->rightchild = new struct tileNode;
            tileNode->rightchild->nodeID = nodeID;
            // set the children to be None
            tileNode->rightchild->rightchild = nullptr;
            tileNode->rightchild->leftchild = nullptr;
            tileNode->name = name;
        }
    }
}

void BST::insert(int nodeID, Tile *tile, string name)
{
    // check to see if anything is in the tree
    if(source_node != nullptr){
        // if true, send to private insert function
        insert(source_node, nodeID, name);
    }else{
        // if the tree is empty, place the root (source_node)
        source_node = new struct tileNode;
        source_node->nodeID = nodeID;
        source_node->tile = tile;
        source_node->leftchild = nullptr;
        source_node->rightchild = nullptr;
        source_node->name = name;
    }
}

//Public
void BST::traverse(tileNode *tileNode)
{

    // if the node is not a null node
    if(tileNode != nullptr)
    {
        //in order traversal
        traverse(tileNode->leftchild);
        cout << tileNode->tile->name << " ";
        traverse(tileNode->rightchild);
    }
}
//public method
int BST::find_node(int nodeID){
    cout << "searching for key: " << nodeID << endl;
    if (source_node != nullptr){
        if (source_node->nodeID == nodeID){ //checks if root is being searched
            cout << "found node in the tree" << endl;
            return 1;
        }
        else {
            find_node(source_node, nodeID); //can optimize in future by searchin rc/lc
        }
    }
    else {
        cout << "this tree is empty" << endl;
        return 0;
    }
    return 1;
}

int BST::find_min(tileNode *node)
{
    //temp node to store ID
    struct tileNode *temp;
    temp = node;
    //loop through all the smallest numbers till you get to the greatest
    while(temp->leftchild != nullptr) {
        temp = temp->leftchild;
    }
    // return the smallest node ID
    return temp->nodeID;
}

int BST::find_max(tileNode *node)
{
    //temp node to store ID
    struct tileNode *temp;
    temp = node;
    //loop through all the greatest numbers till you get to the greatest
    while(temp->rightchild != nullptr) {
        temp = temp->rightchild;
    }
    //return the greatest node ID
    return temp->nodeID;
}

//TODO: FIX TO BE BOOL
//private method
void BST::find_node(tileNode* node, int nodeID){
    if (node->nodeID == nodeID) {
        cout << "found node";
        return;
    }
    else if (node->nodeID > nodeID) {  //checks whether to go right or left
        if (node->leftchild){
            if(node->leftchild->nodeID == nodeID){
                cout << "found key" << endl;
                return;
            }

            else {
                //cout << "searching left child of: " << node->nodeID << endl;
                find_node(node->leftchild, nodeID);
            }
        }
        else {
            cout << nodeID << " is not in the tree" << endl;
            return;
        }
    }
    else if (node->nodeID < nodeID){
        if (node->rightchild){
            if (node->rightchild->nodeID == nodeID){
                cout << "found key " << endl;
                return;
            }
            else {
                //cout << "searching right child of: " << node->nodeID << endl;
                find_node(node->rightchild, nodeID);
            }
        }
        else{
            cout << nodeID << " is not in the tree" << endl;
            return;
        }
    }
}