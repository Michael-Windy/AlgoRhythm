# But what is SAM

Welcome to AlgoRhythm, I'm Mike.

## Introduction and Structure

There is a string. For every substring, we define that "End Position", or "EndPos", is the set of positions where a substring occurs. An "Equal EndPos Class" is the set of substrings with the same EndPos. We can call it "EC". It can be proved that if we sort every substrings in an EC by length, each substring erase the first character is the former string.

SAM, or Suffix Automaton describes the relations of ECs. SAM contains all the information of a string, which means that you can get the original string uniquely from a SAM. It doesn't matter if you don't know what an automaton is.

One node of an SAM representes an EC. There are two kinds of edges, Links and Transitions.

Nodes with Links constructed a tree, Link-Tree. Every Node's EndPos is its father's EndPos's subset. The root's EC only contains empty string, which occurs everywhere. The defination of Link means that when the EC A's string occurs, A's father's string occurs, too. So all of A's father's strings are the suffix of all A's strings.

Nodes with Transitions constructed a DAG. Each Transition has a character as the value. No more than one Transition with the same value could begin from the same node. If there is a Transition from A to B, with the value c, every string from A add a character c in the end can be found in B.

## Construction

SAM can be constructed in linear complexity, both time and space.

We choose the method of addtion. For example, the SAM of the string "BANANA".

Firstly, the SAM of an empty string is a single node "0", representing the EC of the EndPos {0}.

Then, we add the first character "B" into the string. Obviously, the EndPos of the hole new string is definetely new. Because there wasn't the position "1" before. So we creat a new node "1" for the new EC. As a result, the EndPos of the empty string becomes {0,1} instead of {0}. And because the new string is the old string with the addtional character in the end, so we add the Transition "B", from "0" to "1". What about Links? There's only one choice for "1", as {1} is the subset of {0,1}.

Now, add the character "A". Still, create node "2" for the string "BA", add the Transition "A" from "1" to "2". Noticing that string "A" belongs to EC 2, too, so we add the Transition "A" from "0" to "2". Now, EC of {2} contains two strings, "A" and "BA". Obviously, the Link of "2" is still "0".

Every time adding a character C and a node X for the hole new string, we shall deal with Transitions first. It is known that strings in X have a common suffix. Erased the last C, it becomes the common suffix of the ECs that can transit to X. The easiest way to find the ECs that have common suffix is to jump along Links. If the node of the hole old string is Y, the node of the hole new string is X. We jump along Links from Y, every node that doesn't have the Transition C

## Multiple Strings
