import torch
from torch import cuda, bfloat16

import transformers
from transformers import StoppingCriteria, StoppingCriteriaList

class MosaicmlSetUp:

    def __init__(self, device, model_type, task_type):
        self.device = device
        self.model_type = model_type
        self.task_type = task_type

    def model_setup(self, device, model_type):
        model = transformers.AutoModelForCausalLM.from_pretrained(
        self.model_type,
        trust_remote_code=True,
        load_in_8bit=True,
        max_seq_len=1024,
        init_device=device
        )
        model.eval()
        print(f"Model loaded on {self.device}...")
        return model

    def stopping_criteria(self):

        tokenizer = transformers.AutoTokenizer.from_pretrained("mosaicml/mpt-30b")

        stop_token_ids = [
            tokenizer.convert_tokens_to_ids(x) for x in [
                ["Human", ":"], ["AI", ":"]
            ]
        ]

        stop_token_ids = [torch.LongTensor(x).to(device) for x in stop_token_ids]

        class StopOnTokens(StoppingCriteria):
            def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
                for stop_ids in stop_token_ids:
                    if torch.eq(input_ids[0][-len(stop_ids):], stop_ids).all():
                        return True
                return False
            
        stopping_criteria = StoppingCriteriaList([StopOnTokens()])
        return stopping_criteria 

    def generate_text(self, model, task_type, stopping_criteria):
        generate_text = transformers.pipeline(
        model=model,
        return_full_text=True,
        task=self.task_type,
        stopping_criteria=stopping_criteria,
        temperature=0,
        top_p=0.15,
        top_k=0,
        max_new_tokens=500,
        repetition_penality=1.1
        )
        return generate_text
