#!/usr/bin/env python

class Memory (object):
    '''In Memory, each instruction is stored in its binary string format.
    '''

    def __init__ (self, bin_instrn_list = []):
        """Initialize Memory object with a list of binary-string
        instructions.
        """
        self.list = bin_instrn_list

    def __getitem__ (self, memory_addr):
        return self.list [memory_addr / 4]

    def __setitem__ (self, memory_addr, value):
        return self.list.__setitem__ (memory_addr / 4,
                                      value)

    def __iter__ (self):
        return self.list.__iter__ ()

    def __next__ (self):
        return self.list.__next__ ()

    def __len__ (self):
        return self.list.__len__ ()

    @staticmethod
    def get_binary_string(integer, width = 32):
        """Return binary string equivalent of integer.
        
        Arguments:
        - `integer`:
        - `width`:
        """
        # The [2:] is to remove the '0x' prefix.
        return bin (integer) [2:].zfill (width)

    @staticmethod
    def get_bin_from_hex_instruction(hex_instrn_string):
        """Return binary version of the hex instruction string.
        
        Arguments:
        - `hex_instrn_string`:
        """
        hex_integer = int (hex_instrn_string, 16)
        return Memory.get_binary_string(hex_integer)
    
    def set_bin_instruction_list(self, bin_instruction_list):
        """Set bin_instruction_list.
        
        Arguments:
        - `bin_instruction_list`:
        """
        self.list = bin_instruction_list

    def set_hex_instruction_list(self, hex_instruction_list):
        """Set binary instruction list from hex_instruction_list.
        """
        self.list = [Memory.get_bin_from_hex_instruction(instruction)
                     for instruction in hex_instruction_list
                     if instruction.strip()]
        
    def loadProgram (self, program_filename):
        '''Reads a file containing the MIPS code (in hex)
        and loads it into the memory, which can be accessed later. '''
        program_file = open (program_filename)
        lines = program_file.readlines ()
        program_file.close ()
        self.set_hex_instruction_list(lines)

    def loadProgramDebug (self, program_filename):
        program_file = open (program_filename)
        text = program_file.read ()
        program_file.close ()
        self.loadProgramDebugFromText (text)

    def loadProgramDebugFromText (self, text):
        lines = text.split ('\n')
        self.list = [line.strip ().split ()
                     for line in lines
                     if line.strip ()]
        

    def __str__ (self):
        if self.list and type(self.list[0]) == list:
            # print 'Memory __str__: instructions are list of tokens'
            return '\n'.join (str(4 * i) + ' ' + ' '.join(instruction_in_list_format) 
                              for i, instruction_in_list_format in enumerate(self.list))
        return '\n'.join (self.list)

    def __eq__(self, other):
        """Return True iff self and other have the same attributes.
        
        Arguments:
        - `other`:
        """
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

if __name__ == "__main__":
    memory = Memory ()
    memory.loadProgram ('./Input_hex_fibonacci.txt')
    print memory
