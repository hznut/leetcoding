#!python3

#####
# ./count_missing_tags.py
#####

import sys

def countMissingTags(s: str) -> int:
	stack = []
	missing_count = 0
	while len(s) > 0:
		# print(s)
		if s.startswith('<app>'):
			stack.append('<app>')
			s = s[5:]
		elif s.startswith('</app>'):
			if len(stack) == 0:
				missing_count += 1
				s = s[6:]
				continue
			else:	
				popped = stack.pop(-1)
				if popped == '<app>':
					s = s[6:]
					continue
				else:
					missing_count += 1
					s = s[6:]
					continue		
	missing_count += len(stack)
	return missing_count

if __name__ == "__main__":
	# print(countMissingTags(sys.argv[1]))	
	assert countMissingTags('') == 0
	assert countMissingTags('<app>') == 1
	assert countMissingTags('</app>') == 1
	assert countMissingTags('<app></app>') == 0
	assert countMissingTags('<app><app></app>') == 1
	assert countMissingTags('<app></app></app>') == 1
	assert countMissingTags('<app></app><app>') == 1
	assert countMissingTags('<app><app></app></app>') == 0
	assert countMissingTags('<app></app></app></app>') == 2
	assert countMissingTags('<app></app><app><app>') == 2
	assert countMissingTags('</app><app><app>') == 3
