using TwoSum;

Solution s = new Solution();

int[] nums = new int[] { 2, 7, 11, 15 };
int target = 9;

int[] result = s.TwoSum(nums, target);

Console.WriteLine($"[{result[0]}, {result[1]}]");