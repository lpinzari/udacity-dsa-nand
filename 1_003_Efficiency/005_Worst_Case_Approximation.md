# Worst Case and Approximation
Suppose that we analyze an algorithm and decide that it has the following relationship between the input size, `n`, and the number of operations needed to carry out the algorithm:

`N = n^2 +5`


Where `n` is the input size and `N` is the number of operations required.

For example, if we gave this algorithm an input of `2`, the number of required operations would be 2<sup>2</sup> +5 or simply 9.

Below are some other possible values for the input (`n`). For each input, what does n<sup>2</sup> + 5 evaluate to?

| INPUT| Number of operations |
| ------------- |-------------:|
| 5      | 30 |
| 10      | 105 |
| 25 | 630 |
| 100 | 10005 |

The thing to notice in the above exercise, is this: In n<sup>2</sup> + 5, the 5 has very little impact on the total efficiency—especially as the input size gets larger and larger. Asking the computer to do 10,005 operations vs. 10,000 operations makes little difference. Thus, it is the **n<sup>2</sup>** that we really care about the most, and the + 5 makes little difference.

Most of the time, when analyzing the efficiency of an algorithm, the most important thing to know is the **order**. In other words, we care a lot whether the algorithm's time-complexity has a linear order or a quadratic order (or some other order). This means that very often (in fact, most of the time) when you are asked to analyze an algorithm, you can do so by making an **approximation** that significantly simplifies things.

## Resources

- [Big-O-CheatSheet](https://www.bigocheatsheet.com/)

- [Python-Complexity](https://wiki.python.org/moin/TimeComplexity)

- [Python-Complexity-Summary](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
