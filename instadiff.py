# Python script to compare instagram follower and following
# updated 14/1/2019 by Ryan Tan
#
# How to use:
#   1. Install Chrome extension - Helper Tools for Instagram
#      https://chrome.google.com/webstore/detail/helper-tools-for-instagra/hcdbfckhdcpepllecbkaaojfgipnpbpb
#   2. Go to instagram.com/<your-username>.
#   3. Get list of followers and following and save it as "followers.txt" and "following.txt" respectively.
#      * make sure a username a line
#   4. Use python to run this script.

f_followers = open('followers.txt', 'r', encoding="utf8")
f_following = open('following.txt', 'r', encoding="utf8")
files = [f_followers, f_following]

def convert(file, f_set):
    for line in file:
        f_set.add(line.strip('\n'))

followers_set = set()
following_set = set()

convert(f_followers, followers_set)
convert(f_following, following_set)

for opened_file in files:
    opened_file.close()

print('followers', len(followers_set))
print('following', len(following_set))
print()
f_result = open('instadiff_result.txt', 'w')
following_diff = following_set.difference(followers_set)
followers_diff = followers_set.difference(following_set)

f_result.write('followers ' + str(len(followers_set)) + '\n')
f_result.write('following ' + str(len(following_set)) + '\n')
f_result.write('\n')
f_result.write('following but not follower ' + ' ' + str(len(following_diff)) + '\n')
f_result.writelines('%s\n' % l for l in following_diff)
f_result.write('\n')
f_result.write('follower but not following ' + ' ' + str(len(followers_diff)) + '\n')
f_result.writelines('%s\n' % l for l in followers_diff)
print('export to instadiff_result.txt complete!')
f_result.close()
