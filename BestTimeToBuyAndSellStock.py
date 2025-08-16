"""
🛠 Step 1: Brute Force (Naïve Approach)

Idea:
Try all pairs (buy, sell) where buy < sell.
Keep track of the maximum profit.

Code (Brute Force):

def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):          # buy day
        for j in range(i+1, n): # sell day
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


Complexity:

Time: O(n²) → nested loops over all pairs.

Space: O(1).

✅ Works for small input, but impractical for n ~ 10^5.

🛠 Step 2: Optimized Sliding Window / Two Pointers

Key Insight:

The profit on day i is prices[i] - min_price_so_far.

Instead of recomputing all pairs, just maintain:

The minimum price seen so far (best buy).

The maximum profit so far (best sell vs that buy).

Code (Optimized):
"""
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)                   # best day to buy so far
        max_profit = max(max_profit, price - min_price)     # best profit if sold today
    return max_profit

"""
Complexity:

Time: O(n) (single pass).

Space: O(1).

🛠 Step 3: Dry Run Example

Input: prices = [7,1,5,3,6,4]

Day	Price	min_price	price - min_price	max_profit
0	7	7	0	0
1	1	1	0	0
2	5	1	4	4
3	3	1	2	4
4	6	1	5	5
5	4	1	3	5

Answer = 5 (Buy at 1, Sell at 6).

🛠 Step 4: Interview Talking Points

Brute Force: Start with O(n²) to show clarity.

Optimization Insight: Realize you only need min_price and max_profit.

Code: Show the clean min/max version.

Edge Cases:

prices = [7,6,4,3,1] → no profit, return 0.

prices = [1] → no transaction, return 0.

🛠 Step 5: Interview-Ready Answer

🎤 If asked in an interview, you can explain like this:

“At each day, I ask myself: what is the cheapest price I could have bought before today,
and what is the profit if I sell today? I update the best seen so far. 
This reduces the problem from checking all pairs (O(n²)) to a single scan (O(n)), 
while keeping O(1) space. At the end, I return the best profit.”

✅ That’s your polished interview walkthrough.


Would you like me to also add possible follow-up variations the interviewer might ask 
(like “what if multiple transactions are allowed?” → LC 122), so you’re ready for the curveball?
"""
