class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            String curr = tokens[i];
            if (stack.isEmpty()) {
                stack.push(curr);
                continue;
            }
            if (curr.equals("*")) {
                int b = Integer.parseInt(stack.pop());
                int a = Integer.parseInt(stack.pop());
                stack.push(String.valueOf(a*b));
            }
            else if (curr.equals("+")) {
                int b = Integer.parseInt(stack.pop());
                int a = Integer.parseInt(stack.pop());
                stack.push(String.valueOf(a+b));
            } 
            else if (curr.equals("-")) {
                int b = Integer.parseInt(stack.pop());
                int a = Integer.parseInt(stack.pop());
                stack.push(String.valueOf(a-b));
            }else if (curr.equals("/")) {
                int b = Integer.parseInt(stack.pop());
                int a = Integer.parseInt(stack.pop());
                stack.push(String.valueOf(a/b));
            }else {
                stack.push(String.valueOf(curr));
            }
        }
        return Integer.parseInt(stack.pop());
    }
}
