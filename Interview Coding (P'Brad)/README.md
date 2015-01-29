### 1. Reverse each words in the string. Don’t use string reverse function ([reverse_word.py](reverse_word.py))

Input:

```
Hello how Are you
```
Output:

```
olleH woh erA uoy
```

### 1B. Reverse the order of word in the string ([reverse_word_order.py](reverse_word_order.py))
Input:

```
Hello how Are you
```
Output:

```
you Are how Hello
```

### 2. Assume that a product communicate data over a network using a single string. ([serialize-deserialize.py](serialize-deserialize.py))

Create a function to serialize array of String into a single String, so that you can send this string over this network and deserialize to get the same data back.

```
String Serialize(String[] A);
String[] DeSerialize(String data);
```
For example,

```
array A = [ ‘Hello’, ‘123’, ‘$/#’]    ----Serialize--->    String data  so you can send via network.
string data = …..........   ----DeSerialize--->   array A    so you can get the original array back
```

How would you design the data string?
Implement serialize and deserialize

### 3. Input: two binary search tree
Output: a merged binary search tree
Explain algorithm and complexity. No need to code it, but it’s fine if you want to practise coding