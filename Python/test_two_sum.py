import unittest
import os
import time
import re

class TestTwoSum(unittest.TestCase):
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
                    # Extract numbers array using regex
                    numbers_match = re.search(r'numbers\s*=\s*\[(.*?)\]', line)
                    if numbers_match:
                        numbers_str = numbers_match.group(1)
                        current_case['numbers'] = [int(x.strip()) for x in numbers_str.split(',')]
                    
                    # Extract target using regex
                    target_match = re.search(r'target\s*=\s*(-?\d+)', line)
                    if target_match:
                        current_case['target'] = int(target_match.group(1))
                        
                elif line.startswith('Output:'):
                    # Extract output array using regex
                    output_match = re.search(r'\[(.*?)\]', line)
                    if output_match:
                        output_str = output_match.group(1)
                        current_case['expected'] = [int(x.strip()) for x in output_str.split(',')]
                        test_cases.append(current_case)
                        current_case = {}
                i += 1
                
        return test_cases

    def test_two_sum_cases(self):
        start_time = time.time()
        test_cases = self.parse_test_cases()
        
        # Clear output file before writing new results
        with open(self.output_file, 'w') as f:
            pass
            
        import traceback
        for i, case in enumerate(test_cases, 1):
            try:
                # Write input case to output file
                with open(self.output_file, 'a') as f:
                    f.write(f"Case {i}:\n")
                    f.write(f"Input: numbers = {case['numbers']}, target = {case['target']}\n")
                    f.write(f"Expected Output: {case['expected']}\n")
                    f.write("Status: Skipped (Solution not implemented)\n\n")

            except Exception as exc:
                tb = traceback.format_exc()
                with open(self.output_file, 'a') as f:
                    f.write(f"Case {i}:\n")
                    f.write(f"Input: numbers = {case['numbers']}, target = {case['target']}\n")
                    f.write(f"Error: {str(exc)}\n")
                    f.write("Traceback:\n")
                    f.write(tb)
                    f.write("Result: Error\n\n")
                with self.subTest(f"Test case {i}"):
                    self.fail(f"Exception while processing case {i}: {exc}\n{tb}")
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Write execution time to sys.txt
        with open(self.sys_file, 'w') as f:
            f.write(f"{execution_time:.6f} seconds\n")

if __name__ == '__main__':
    unittest.main()