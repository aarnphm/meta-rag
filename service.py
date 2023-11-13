import bentoml
from llama_index.llms.openllm import OpenLLMAPI

llm = OpenLLMAPI()

svc = bentoml.Service('openllm-rag', runners=[llm.runner])


@svc.api(input=bentoml.io.JSON(), output=bentoml.io.Text())
async def rag(self, input):
  # TODO: preprocessing
  return await llm.acomplete(input)


if __name__ == '__main__':
  bentoml.HTTPServer(svc).start(blocking=True)
