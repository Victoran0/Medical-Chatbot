# Medical ChatBot Using Llama 3.1

If you are using Llama Cpp on windows with Nvidia GPU, the below is required: \
read the documentation https://python.langchain.com/v0.2/docs/integrations/llms/llamacpp/ \
After setting your environment variables, It is advisable to install the version below instead of cloning the Github repo in the documentation: \

```bash
pip install llama-cpp-python==0.2.51 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121
```

Where 121 is is cuda version 12.1 (you can specify the version you want from 12.1-12.4)
But if you try the repo version (latest) and it works just fine, then you have no problems!!!
