


stack = []


stack.append(1)
stack.append(2)
stack.append(3)


print(stack)

final_elements = stack.pop()
stack.pop()
stack.pop()
print(final_elements)


if not stack:
    print("empty stack")