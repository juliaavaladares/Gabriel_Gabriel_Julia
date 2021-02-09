from chatterbot.logic import LogicAdapter
import re



class MyLogicAdapter(LogicAdapter):

    def can_process(self, statement):
        with open('ques_ans.txt') as f:
            for line in f:
                line = line.rstrip()  # remove '\n' at end of line
                if statement == line:
                    print(next(line))

    def process(self, input_statement):

        # For this example, we will just return the input as output
        selected_statement = can_process(self, input_statement)
        response = sele

        return selected_statement