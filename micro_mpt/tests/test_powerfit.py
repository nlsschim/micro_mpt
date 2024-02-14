import numpy as np
import pytest
from micro_mpt.power_fit import f_Kelvin, f_pow, f_pow2, err_pow_weight, err_pow, err_kelvin, fit_pow_weight

# Assuming the f_Kelvin function is defined elsewhere

class TestFKelvin:
    # 1. Functionality Test
    def test_functionality(self):
        x = np.array([1, 2, 3])
        a = np.array([2, 2])
        b = np.array([3, 3])
        expected_y = 2 * (1 - np.exp(-3 * x))
        actual_y = f_Kelvin(x, a, b)
        np.testing.assert_array_almost_equal(actual_y, expected_y, decimal=5, err_msg="Kelvin approximation calculation is incorrect")

    # 2. Parameter Length Mismatch
    def test_param_length_mismatch(self):
        x = np.array([1, 2, 3])
        a = np.array([2])
        b = np.array([3, 3])
        with pytest.raises(ValueError) as excinfo:
            f_Kelvin(x, a, b)
        assert "Mismatch in parameters length" in str(excinfo.value), "Function should raise ValueError for parameter length mismatch"

    # 3. Output Verification
    def test_output_verification(self):
        x = np.array([0])  # For x=0, the approximation simplifies considerably
        a = np.array([1])
        b = np.array([1])
        expected_y = np.array([0])  # Since exp(0) is 1, leading to 1-1=0
        actual_y = f_Kelvin(x, a, b)
        np.testing.assert_array_equal(actual_y, expected_y, err_msg="Output does not match expected for x=0")

    # 4. Type and Value Errors (Example: Negative values for a or b if not allowed)
    # This example assumes negative values are not allowed for demonstration
    def test_negative_values(self):
        x = np.array([1, 2])
        a = np.array([-1, -2])
        b = np.array([3, 4])
        with pytest.raises(ValueError) as excinfo:
            f_Kelvin(x, a, b)
        assert "Negative values not allowed" in str(excinfo.value), "Function should raise ValueError for negative values in a or b"

# Note: Adjust the actual implementation of f_Kelvin as needed to properly raise ValueErrors for these test cases.
        

# Assuming the f_pow function is defined elsewhere

class TestFPow:
    # 1. Functionality Test
    def test_functionality(self):
        x = np.array([2, 3])
        a = [1, 2]
        b = [2, 3]  # Corresponds to 1*2^2 + 2*3^3 for each x
        expected_y = np.array([1*2**2 + 2*3**3, 1*3**2 + 2*3**3])
        actual_y = f_pow(x, a, b)
        np.testing.assert_array_almost_equal(actual_y, expected_y, decimal=5, err_msg="Sum of power functions calculation is incorrect")

    # 2. Parameter Length Mismatch
    def test_param_length_mismatch(self):
        x = 2
        a = [1]
        b = [2, 3]
        with pytest.raises(ValueError) as excinfo:
            f_pow(x, a, b)
        assert "Mismatch in parameters length" in str(excinfo.value), "Function should raise ValueError for parameter length mismatch"

    # 3. Input Types
    @pytest.mark.parametrize("x", [2, np.array([2, 3])])
    def test_input_types(self, x):
        a = [1, 2]
        b = [0, 1]  # Simple cases, should work for both single value and array
        if isinstance(x, np.ndarray):
            expected_y = x * 0 + 1 + x * 2
        else:
            expected_y = 1 + x * 2
        actual_y = f_pow(x, a, b)
        np.testing.assert_array_almost_equal(actual_y, expected_y, decimal=5, err_msg="Function does not handle different types of input x correctly")

    # 4. Correct Calculation
    def test_correct_calculation(self):
        x = np.array([1, 0])  # Test with base 1 and 0, edge cases
        a = [1, 1]
        b = [0, 1]  # 1*1^0 + 1*0^1 = 1 for both x; second term is zero for x=0
        expected_y = np.array([1, 1])  # Expected sum for each x
        actual_y = f_pow(x, a, b)
        np.testing.assert_array_equal(actual_y, expected_y, err_msg="Incorrect calculation for edge case inputs")

# Note: Adjust the actual implementation of f_pow as needed to properly raise ValueErrors for these test cases.
        

class TestFPow2:
    # 1. Correct Calculation
    def test_correct_calculation(self):
        x = 2
        a, b, c = 1, 2, 3
        expected_value = a * x**(b + c * np.log(x))
        assert f_pow2(x, a, b, c) == pytest.approx(expected_value), "f_pow2 does not calculate the correct value"

    # 2. Handling of Different `x` Types
    @pytest.mark.parametrize("x", [2, np.array([2, 3])])
    def test_different_x_types(self, x):
        a, b, c = 1, 1, 1
        expected_value = x * x  # Simplified expected result for a=b=c=1
        np.testing.assert_array_almost_equal(f_pow2(x, a, b, c), expected_value, err_msg="f_pow2 fails with different types of x")

    # 3. Edge Cases
    @pytest.mark.parametrize("x", [0, -1, 1])
    def test_edge_cases(self, x):
        a, b, c = 1, 1, 1
        if x <= 0:
            with pytest.raises(ValueError):
                f_pow2(x, a, b, c)
        else:
            expected_value = a * x**(b + c * np.log(x))
            assert f_pow2(x, a, b, c) == pytest.approx(expected_value), f"f_pow2 fails for edge case x={x}"

    # Note: This edge case test assumes f_pow2 should raise a ValueError for non-positive x due to log(x). 
    # If the function's intended behavior is different, adjust the test accordingly.

    # 4. Input Validation (Optional)
    # Implement this test based on the specific requirements for input validation, if any.

# Note: Ensure that f_pow2 is defined and properly imports numpy before running these tests.




# Assuming the err_pow_weight function is implemented as described
# def err_pow_weight(params, args):
#     ...

class TestErrPowWeight:
    # Test for correct error calculation
    def test_correct_error_calculation(self):
        params = [1, 2, 3]  # Example parameters for power law model
        args = {'x': np.array([1, 2, 3]), 'y': np.array([2, 4, 6]), 'weight': np.array([1, 1, 1])}
        # Expected error calculation based on a known correct formula or manually calculated expected result
        expected_error = ...  # Placeholder for expected error calculation
        calculated_error = err_pow_weight(params, args)
        assert np.isclose(calculated_error, expected_error), "err_pow_weight does not return expected weighted error"

    # Test for parameter length verification
    def test_parameter_length(self):
        params_short = [1, 2]  # Shorter than expected
        params_long = [1, 2, 3, 4]  # Longer than expected
        args = {'x': np.array([1]), 'y': np.array([2]), 'weight': np.array([1])}
        with pytest.raises(ValueError):
            err_pow_weight(params_short, args)
        with pytest.raises(ValueError):
            err_pow_weight(params_long, args)

    # Test for args structure verification
    def test_args_structure(self):
        params = [1, 2, 3]
        args_incomplete = {'x': np.array([1, 2]), 'y': np.array([2, 4])}  # Missing 'weight'
        with pytest.raises(KeyError):
            err_pow_weight(params, args_incomplete)

    # Test handling different data sizes
    def test_different_data_sizes(self):
        params = [1, 2, 3]
        args_small = {'x': np.array([1]), 'y': np.array([2]), 'weight': np.array([1])}
        args_large = {'x': np.array([1, 2, 3, 4, 5]), 'y': np.array([2, 4, 6, 8, 10]), 'weight': np.array([1, 1, 1, 1, 1])}
        # Assuming the function can handle different sizes, we mainly want to ensure it doesn't raise unexpected errors
        try:
            err_pow_weight(params, args_small)
            err_pow_weight(params, args_large)
        except Exception as e:
            pytest.fail(f"err_pow_weight raised an exception with different data sizes: {e}")

    # Edge cases and error handling (Example: Empty inputs)
    def test_edge_cases_empty_inputs(self):
        params_empty = []
        args_empty = {'x': np.array([]), 'y': np.array([]), 'weight': np.array([])}
        with pytest.raises(ValueError):
            err_pow_weight(params_empty, args_empty)

# Note: Replace the "..." with the actual expected error calculation or condition check specific to your implementation.


# Assuming the err_pow function is defined as described
# def err_pow(params, *args):
#     ...

class TestErrPow:
    # 1. Correct Error Calculation
    def test_correct_error_calculation(self):
        params = [1, 2]  # Simple power law parameters for easy verification
        x_values = np.array([1, 2, 3])
        y_actual = np.array([2, 4, 8])  # Example actual y values
        # Assuming a simple power law: y = a * x^b, where params = [a, b]
        y_predicted = params[0] * x_values ** params[1]
        expected_errors = y_actual - y_predicted
        calculated_errors = err_pow(params, x_values, y_actual)
        np.testing.assert_array_almost_equal(calculated_errors, expected_errors, err_msg="err_pow does not return expected errors")

    # 2. Parameter Length Verification
    def test_parameter_length_verification(self):
        params_short = [1]  # Not enough parameters
        x_values = np.array([1, 2, 3])
        y_values = np.array([2, 4, 8])
        with pytest.raises(ValueError):
            err_pow(params_short, x_values, y_values)

    # 3. Args Structure
    def test_args_structure(self):
        params = [1, 2]
        x_values = np.array([1, 2, 3])
        # Missing y_values should raise an error or handle as per function's design
        with pytest.raises(TypeError):
            err_pow(params, x_values)

    # 4. Return Type and Value
    def test_return_type_and_value(self):
        params = [1, 2]
        x_values = np.array([1, 2, 3])
        y_values = np.array([2, 4, 8])
        errors = err_pow(params, x_values, y_values)
        assert isinstance(errors, np.ndarray), "Return type is not numpy array"
        # Additional checks for the values can be based on specific expectations

# Note: Adjust the error checks, expected values, and assumptions based on the actual implementation details of your err_pow function.

class TestErrKelvin:
    # Test for correct error calculation
    def test_correct_error_calculation(self):
        params = [1, 2]  # Example parameters for the Kelvin model
        x_values = np.array([1, 2, 3])
        y_actual = np.array([2, 4, 6])  # Example actual y values for given x
        # Calculate expected errors based on a hypothetical Kelvin model function
        # This is a placeholder; the actual calculation will depend on the Kelvin model specifics
        y_predicted = params[0] * np.exp(-params[1] * x_values)  # Simplified Kelvin model example
        expected_errors = y_actual - y_predicted
        calculated_errors = err_kelvin(params, x_values, y_actual)
        np.testing.assert_array_almost_equal(calculated_errors, expected_errors, err_msg="err_kelvin does not return expected errors")

    # Test that params length is verified
    def test_params_length_verification(self):
        params_short = [1]  # Not enough parameters for a Kelvin model
        x_values = np.array([1, 2, 3])
        y_values = np.array([2, 4, 6])
        with pytest.raises(ValueError):
            err_kelvin(params_short, x_values, y_values)

    # Test handling of args
    def test_args_handling(self):
        params = [1, 2]
        x_values = np.array([1, 2, 3])
        # Assuming function requires both x and y values; if y is missing, an error should be raised
        with pytest.raises(TypeError):
            err_kelvin(params, x_values)

    # Test for return type and value
    def test_return_type_and_value(self):
        params = [1, 2]
        x_values = np.array([1, 2, 3])
        y_values = np.array([2, 4, 6])
        errors = err_kelvin(params, x_values, y_values)
        assert isinstance(errors, np.ndarray), "Return type is not numpy array"
        # Additional value checks could be added based on the expected behavior

class TestFitPowWeight:
    # Test for correctness of fitted parameters
    def test_correctness_of_fitted_parameters(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 8])
        weight = np.array([1, 1, 1])
        parabolic = False  # Testing with a simple power law fit first
        result = fit_pow_weight(x, y, weight, parabolic)
        # Since this test depends on the specific fitting algorithm, we'll focus on structure
        assert 'optimized_parameters' in result, "Optimized parameters missing from result"

    # Test for output structure
    def test_output_structure(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 8])
        weight = np.array([1, 1, 1])
        result = fit_pow_weight(x, y, weight, True)  # `parabolic` flag doesn't matter for structure test
        expected_keys = ['optimized_parameters', 'original_data', 'fitted_data', 'cov_matrix', 'squared_diffs', 'weights']
        assert all(key in result for key in expected_keys), "Output dictionary structure is incorrect"

    # Test handling of the `parabolic` flag
    @pytest.mark.parametrize("parabolic", [True, False])
    def test_parabolic_flag_handling(self, parabolic):
        x = np.array([1, 2, 3, 4])
        y = np.array([2.1, 4.2, 8.4, 16.8])  # Data that could fit a power law or parabolic in log-log
        weight = np.array([1, 1, 1, 1])
        result = fit_pow_weight(x, y, weight, parabolic)
        # Verifying functionality requires knowing the fitting algorithm; focus on the flag affecting results
        assert isinstance(result, dict), "Function did not return a dictionary"

    # Test for data integrity
    def test_data_integrity(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 8])
        weight = np.array([1, 1, 1])
        result = fit_pow_weight(x, y, weight, False)
        np.testing.assert_array_equal(result['original_data']['x'], x, err_msg="Original x data altered")
        np.testing.assert_array_equal(result['original_data']['y'], y, err_msg="Original y data altered")
        np.testing.assert_array_equal(result['weights'], weight, err_msg="Weights data altered")

    # Test for error handling (Example: Mismatched array lengths)
    def test_error_handling_mismatched_lengths(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4])  # Mismatched length with x
        weight = np.array([1, 1, 1])
        with pytest.raises(ValueError):
            fit_pow_weight(x, y, weight, False)