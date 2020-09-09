Leetcode 题解   

公式的表示方法：   
因为markdown需要装插件才能显示公式，因此这里计划用google的服务（`![](http://chart.googleapis.com/chart?cht=tx&chl= 在此插入Latex公式)`）

## 1

### two sum

有一个序列`nums`和一个数字`target`,求序列中的两个元素**下标**，使其对应元素和为`target`。

#### 例

* * `input`:[2, 7, 11, 15], target = 9
  * `output`: [0, 1]

* * `input`:[0,3 ,2 ,0], target = 0

  * `output`: [0, 3]

* * `input`:[0,3 ,-3 ,1], target = 0

  * `output`: [1, 2]    

#### 思路

枚举的时候，可以先把数字和位置用hash存起来，后面遇到新的数字，访问一下字典看有没有和它配对的数字。这只需要`O(n)`就能完成。

进一步的，因为只有两个数字，在遍历第一个数字的时候，把第一个数字的位置存在第二个数字处，即:

```python
dict[target - value] = index
```

这样节省了几个判断，可以有效提高效率。



## 4

两个排序好的序列`num1`（长度为m）和`num2`（长度为n）。

求两个序列的中位数(`median`)

时间复杂度要求：$O(\log{(m+n)})$

思路




## 5

回文

假设$f(i,j)$  表示$s_is_{i+1}...s_{j-1}s_{j}$ 是一个回文串。

那么迁移方程就是：
$$
f(i,j) =\ s(i)==s(j) \ \ and \ \ f(i+1,j-1)\\
f(i,i+1) = s(i)==s(i) 
$$
边界：
$$
f(i,i) = 1\\
$$
另外需要注意的是，$i$是大的方向获得的；$j$是从小的方向获得的。因此迭代的时候要注意i要逆向迭代。
## 53
## 516

最长回文子串

给定一个字符串$s$，找到其中最长回文子串（`longest palindromic subsequence`）的长度。

### DP解法

用$f(i,j)$ 表示从字符$i$ 到$j$ 最长的回文子串的长度。那么如果可以拓展的话（刚好找到一对相同的字符），直接加上2拓展即可；如果不能拓展，就找之前子集中最大的。
$$
f(i,j) =\left\{  
 \begin{array}{**lr**}
f(i+1,j-1)+2,&s_i=s_j\\
\max(f(i+1,j),f(i,j-1)),&s_i\not=s_j
\end{array}
\right.
$$
