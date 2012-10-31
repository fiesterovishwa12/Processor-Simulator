from stage_buffer import StageBuffer

class FetchInputBuffer(StageBuffer):
    """Buffer for storing input to the Fetch stage.
    """

    arg_list = [
        'PC',
        'is_branch_reg_zero',
        'branch_target_pc',
        'instr_count',
        ]
    
    def __init__(self, input_dict = {}):
        """
        """
        super(FetchInputBuffer, self).__init__(input_dict)
