class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        return max(
            (
                kv1[1] + kv2[1] + 1
                for kv1, kv2 in pairwise(
                    (k, len(list(v)))
                    for k, v in groupby(
                        (a2 - a1 for a1, a2 in pairwise(arr)),
                        lambda x: "p" * (x > 0) + "n" * (x < 0),
                    )
                )
                if kv1[0] == "p" and kv2[0] == "n"
            ),
            default=0,
        )