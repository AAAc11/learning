def build_pc(cpu,gpu,**opcjonalne):
    d1={'cpu': cpu, 'gpu': gpu}
    d1.update(opcjonalne)
    return d1



print(build_pc(cpu="1",gpu="2",ram=16,dysk="1TB"))