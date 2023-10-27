## Architecture

```
┌──────────────────────┐   ┌───────────────────────┐
│ declare block_url 1G │───│   C module: shm_zone  │
└──────────────────────┘   └───────────────────────┘
           │                           │            
┌──────────────────────┐   ┌───────────────────────┐
│  write to block_url  │───│   stage: init_by_lua  │
└──────────────────────┘   └───────────────────────┘
           │                           │            
┌──────────────────────┐   ┌───────────────────────┐
│   read from block_url│───│  stage: access_by_lua │
└──────────────────────┘   └───────────────────────┘
```

## 1. Declare block_url

```
block_url 1G
```

### 1.1 Hello world C module

> Tips: Write and Compile

References: [nginx-shared-memory-module](https://github.com/friparia/nginx-shared-memory-module)

### 1.2 Moving to Hashmap

> Tips: using RWlock to get and write

### 1.3 Wrap C structure with lua structure

> Tips: lua gets data from the module in access stage

### 1.4 Test the nginx c module

## 2. write to block_url

> Tips: call write interface

## 3. Read from block_url

## References

1. [nginx-shared-memory-module](https://github.com/friparia/nginx-shared-memory-module)
2. [ngx_shmap](https://github.com/jie123108/ngx_shmap)