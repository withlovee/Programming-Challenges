# Cooking the Books (15 points)

Source: [https://www.facebook.com/hackercup/problems.php?pid=582062045257424&round=742632349177460](https://www.facebook.com/hackercup/problems.php?pid=582062045257424&round=742632349177460)

Every business can make use of a good accountant and, if they're not big on following the law, sometimes a bad one. Bad accountants try to make more money for their employers by fudging numbers without getting caught.

Sometimes a bad accountant wants to make a number larger, and sometimes smaller. It is widely known that tax auditors will fail to notice two digits being swapped in any given number, but any discrepancy more egregious will certainly be caught. It's also painfully obvious when a number has fewer digits than it ought to, so a bad accountant will never swap the first digit of a number with a 0.

Given a number, how small or large can it be made without being found out?

### Input
Input begins with an integer T, the number of numbers that need tweaking. Each of the next T lines contains a integer N.

### Output
For the ith number, print a line containing "Case #i: " followed by the smallest and largest numbers that can be made from the original number N, using at most a single swap and following the rules above.

### Constraints
1 ≤ T ≤ 100 
0 ≤ N ≤ 999999999 
N will never begin with a leading 0 unless N = 0

#### Example Input
[Download](https://www.facebook.com/ajax/hackercup/example?pid=582062045257424&type=input)

```
5
31524
897
123
10
5
```


#### Example Output
[Download](https://www.facebook.com/ajax/hackercup/example?pid=582062045257424&type=output)

```
Case #1: 13524 51324
Case #2: 798 987
Case #3: 123 321
Case #4: 10 10
Case #5: 5 5
```