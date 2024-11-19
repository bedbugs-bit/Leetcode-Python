from collections import defaultdict, Counter

def get_recommended_friends(num, friendships):
    # Build the adjacency list
    graph = defaultdict(set)
    for u, v in friendships:
        graph[u].add(v)
        graph[v].add(u)

    # List to store recommendations for each user
    recs_list = [-1] * num

    # Iterate over each user
    for i in range(num):
        # Counter to count potential friends and their common friend count
        potential_friend_count_list = Counter()

        # Iterate over the user's friends
        for friend in graph[i]:
            # Look at the friend's friends
            for second_friend in graph[friend]:
                # Add to counter if valid recommendation
                if second_friend != i and second_friend not in graph[i]:
                    potential_friend_count_list[second_friend] += 1

        # Variables to track the best recommendation
        highest_num_common_friends = -1
        best_recommendation = -1

        # Find the best recommendation
        for candidate, count in potential_friend_count_list.items():
            if (count > highest_num_common_friends or
                    (count == highest_num_common_friends and candidate < best_recommendation)):
                highest_num_common_friends = count
                best_recommendation = candidate

        # Update the recommendation list for this user
        recs_list[i] = best_recommendation

    return recs_list
