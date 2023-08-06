# But what is SAM

Welcome to AlgoRhythm, I'm Mike.

## Introduction and Structure

There is a string. For every substring, we define that "End Position", or "EndPos", is the set of positions where a substring occurs. An "Equal EndPos Class" is the set of substrings with the same EndPos. We can call it "EC". It can be proved that if we sort every substrings in an EC by length, each substring erase the first character is the former string.

---

SAM, or Suffix Automaton describes the relations of ECs. SAM contains all the information of a string, which means that you can get the original string uniquely from a SAM.

One node of an SAM representes an EC. There are two kinds of edges, Links and Transitions.

Nodes with Links constructed a tree, Link-Tree. Every Node's EndPos is its father's EndPos's subset. The root's EC only contains empty string, which occurs everywhere. The definition of Link means that when the EC A's string occurs, A's father's string occurs, too. So all of A's father's strings are the suffix of all A's strings.

---

Nodes with Transitions constructed a DAG. Each Transition has a character as the value. No more than one Transition with the same value could begin from the same node. If there is a Transition from A to B, with the value c, every string from A add a character c in the end can be found in B.

---

## Construction

SAM can be constructed in linear complexity, both time and space.

We choose the method of addtion.

Everytime we add a character at the end of the string, the new string will have a set of new substrings. Clearly, these substrings are suffixes, and can be arranged as a triangle.

We divide the triangle, and except the tip, there are lots of trapezoidals. Let strings with the same EndPos in a same trapezoidal, representing the EndPos's node. 

Note that current whole string's node is X. When adding a character C, a new node should be added. We define the new node is N. From X, jump along Links, if there is no Transition with the value C, create a new Transition from current node to N, if there is already a Transition with value C, note the node as Y, the node that Y's Transition C pointing at is T.

Because every node have series of strings, we define the length of a node is the length of the longest string in the node. So the length of Y is the length of X plus 1. Define that Y's length is $y$, T's length is $t$. If $t = y + 1$, we can let N's Link point at T.

If not, split T as T1 and T2. So the Transitions used to point at T should point at T1 or T2. Let strings longer than $y + 1$ belongs to T2, so the former Transitions' beginings whose length is longer than $y$ should point at T2. The rest of those strings belongs to T1, and the rest of those former Transitions should point at T1. So the length of T1 is $y + 1$, and the length of the shortest string in T2 is $y + 2$. Former Transitions that begings from T, should be copied, both T1 and T2 should have these Transitions. T1's Link is former T's Link.

We know that on the Link Tree, From X to T's son, their Transitions of C all point at N. So N's shortest string's length is $(y + 1) + 1 = y + 2$, and T2's shortest string's length is $y + 2$, too. Then, as T1's length is $y + 1$, so N and T2's Link is T1.

## Explain

Back to the triangle constructed with new suffixes while adding a new character.

We divide the triangle, and the top of the triangle can be devided as existing SAM nodes. So we just take care of the bottom.

However, sometimes only a part of the existing node can match with the devided triangle, which means that the Endpos of the strings of the node are no longer the same. The matched part has a new occuring position, and the unmathed part's Endpos doesn't change. So as the defination of a Node: "Every string in one Node has the same Endpos", the Node should split.

For an added node N, transitions links to it are very easy to find. Because those Transitions' beginnings, can be proved to have some same Endpos elements, which shift right by one character is a subset of N's EndPos. So we just go through the Links to find every Transitions.

When we going through the Links, adding the Transitions, we may find from a Node X already has Transition of the same character, pointing at the suffix of the current Node. Then we find the current Node's Link. If not every strings in X are the suffix of the current Node, as we explained above, X should split, and the upper part is the Link of the lower part and the current Node.

## Practice

For example, the SAM of the string "BANANA". Here is the whole construction of the SAM of the string "BANANA".

