from typing import List
import unittest
import time
import os
import ast

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    return


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Get the path to input.txt relative to this test file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        self.input_file = os.path.join(root_dir, 'input.txt')
        self.output_file = os.path.join(root_dir, 'output.txt')
        self.sys_file = os.path.join(root_dir, 'sys.txt')
        
    def parse_test_cases(self):
        test_cases = []
        current_case = {}
        
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith('Input:'):
                    # Extract input string
                    s = line.split('=')[1].strip().strip('"')
                    current_case['input'] = s
                    # current_case['input'] = ast.literal_eval(input())
                elif line.startswith('Output:'):
                    # Convert output string to boolean
                    output = line.split(':')[1].strip().lower() == 'true'
                    current_case['expected'] = output
                    test_cases.append(current_case)
                    current_case = {}
                i += 1
                
        return test_cases

    def test_palindrome_cases(self):
        start_time = time.time()
        test_cases = self.parse_test_cases()
        
        # Clear output file before writing new results
        with open(self.output_file, 'w') as f:
            pass
            
        import traceback
        for i, case in enumerate(test_cases, 1):
            # Run each case and handle unexpected exceptions so other cases proceed
            case_start_time = time.time()
            try:
                result = is_palindrome(case['input'])
            except Exception as exc:
                tb = traceback.format_exc()
                with open(self.output_file, 'a') as f:
                    f.write(f"Case {i}:\n")
                    f.write(f"Input: s = \"{case['input']}\"\n")
                    f.write(f"Error: {str(exc)}\n")
                    f.write("Traceback:\n")
                    f.write(tb)
                    f.write("Result: Error\n\n")
                # Record the failure in the unittest framework but continue to next case
                with self.subTest(f"Test case {i}"):
                    self.fail(f"Exception while processing input '{case['input']}': {exc}\n{tb}")
                # continue to next test case (the self.fail above marks this subtest failed)
                # continue

            # Normal result – append to output file
            with open(self.output_file, 'a') as f:
                f.write(f"Case {i}:\n")
                f.write(f"Input: s = \"{case['input']}\"\n")
                f.write(f"Output: {str(result).lower()}\n")
                f.write(f"Time: {time.time() - case_start_time:.6f} seconds\n")
                if result == case['expected']:
                    f.write("Result: Passed\n")
                else:
                    f.write(f"Result: Failed (Expected: {case['expected']})\n")
                f.write("\n")

            with self.subTest(f"Test case {i}"):
                self.assertEqual(
                    result,
                    case['expected'],
                    f"Failed for input '{case['input']}'. Expected {case['expected']}, got {result}"
                )
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Write execution time to sys.txt
        with open(self.sys_file, 'w') as f:
            f.write(f"{execution_time:.6f} seconds\n")

if __name__ == '__main__':
    unittest.main()