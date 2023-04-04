# CycleGAN in PyTorch

## 1.简介

该项目是基于PyTorch的CycleGAN运行程序，通过这个项目实现图片的风格转换

参考[ Jun-Yan Zhu的项目](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

## 2.环境准备

- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

需要PyTorch以及其他运行库（如torchvison，visdom和dominate）

**建议用以下命令**

```
pip环境:
pip install -r requirements.txt

conda环境：
conda env create -f environment.yml
```

## 3.部分重要文件夹

### 3.1 datasets

​	datasets文件夹存放数据集，在本项目中，请将其结构设置如下

```
-datasets
--tank
---testA		（在这个文件夹中放入测试数据集A）
---testB		（在这个文件夹中放入测试数据集B）
---trainA		（在这个文件夹中放入训练数据集A）
---trainB		（在这个文件夹中放入训练数据集B）
```



### 3.2 checkpoints

​	checkpoints文件夹存放训练好的模型，在使用默认参数的情况下，每5个epoch保存一次模型，可以手动调取任意一个进行使用。文件夹结构如下

```
-checkpoints
--tank_cyclegan
---web		（该文件夹内存放训练过程中生成图片）
----images		（训练过程中生成的图片）
----index.html		（生成图片的集合html文件，可以通过这个查看模型效果）
---5_net_D_A.pth		（历代模型）
---5_net_D_B.pth
---5_net_G_A.pth
---5_net_G_B.pth
--- ……
---latest_net_D_A.pth		（最后一次保存的模型）
---latest_net_D_A.pth
---latest_net_D_A.pth
---latest_net_D_A.pth
---loss_log.txt		（loss值变化）
---test_opt.txt		（测试参数）
---train_opt.txt		（训练参数）
```

### 3.3 results

​	results文件夹保存测试结果，测试程序会将生成的图片汇总成一个html文件，方便查看。

## 4.训练和测试

### 4.1数据集下载

~~[百度网盘（提取码h7m0）](https://pan.baidu.com/s/11L3ztsnWlRQA0TukOkr1Kw) 包含个人筛选出的六个风格的装甲车图片，用于本项目的训练~~

- ~~本压缩包中包含六个文件夹，每个文件夹为不同风格的坦克图片，并且分为test和train两个子文件夹，进行训练前请手动将图片移动到程序datasets内对应的文件夹中~~

请看**总目录**中的数据集地址

### 4.2训练命令

在训练开始前，建议启动visdom可视化工具。不启动也可以开始训练，但是程序会频繁警告。

```
python -m vidsom.server
```

训练命令如下：

```python
python train.py 
--dataroot ./datasets/tank 
--name maps_cyclegan 
--model cycle_gan
```

dataroot后输入训练数据集的路径；name后输入训练完毕后输出模型的名称；

训练完成后模型位置在根目录checkpoints文件夹中

**若无其他要求训练，直接复制该命令即可**

### 4.3测试模型

```python
python test.py 
--dataroot ./datasets/tank 
--name tank_cyclegan 
--model cycle_gan
```

dataroot后输入测试集路径；name后输入已经训练完毕的模型文件夹名称；也可在[该链接](http://efrosgans.eecs.berkeley.edu/cyclegan/pretrained_models) 获得已经预训练好的模型，放入checkpoints文件夹中直接使用（**总目录**中包含已训练好的装甲车数据集模型）

也可以进行单边测试，其中‘--model test’控制仅生成单边图像

```python
python test.py 
--dataroot datasets/tank/testA 
--name tank_cyclegan 
--model test 
--no_dropout
```

测试结果放在results文件夹中

## 5.报错和警告

1. **UserWarning: Detected call of `lr_scheduler.step()` before `optimizer.step()`. In PyTorch 1.1.0 and later, you should call them in the opposite order: `optimizer.step()` before `lr_scheduler.step()`.  Failure to do this will result in PyTorch skipping the first value of the learning rate schedule.** 

   pytorch1.1.0之后，优化器的更新要放到学习率更新的前面，实际上不影响程序运行
   
2. **HTTPConnectionPool(host='localhost', port=8097): Max retries exceeded with url: /env/main (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000281B4B1FBA8>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。',))**
   **[WinError 10061] 由于目标计算机积极拒绝，无法连接。**
   **on_close() takes 1 positional argument but 3 were given**
   **Visdom python client failed to establish socket to get messages from the server. This feature is optional and can be disabled by initializing Visdom with `use_incoming_socket=False`, which will prevent waiting for this request to timeout.**

   visdom可视化没有打开


3. **CUDA out of memory** 

4. **训练图片出现红绿色乱码**
   
   这两个问题都大概率是CUDA和pytorch版本问题，请安装环境时务必使用本文”2.环境准备“中的命令，安装和原作者相同的环境，pytorch最新版本和之前的版本部分函数编写方式不同，使用最新版pytorch会导致程序可以运行但是效果极差。

6. **UserWarning: Argument interpolation should be of type InterpolationMode instead of int. Please, use InterpolationMode enum.**
   **“Argument interpolation should be of type InterpolationMode instead of int.** 

   在base_dataset添加InterpolationMode，并代替PIL.Image。

   定位到dataset的transform里(base_dataset.py)，添加引用，然后改一下

   ```
   from torchvision.transforms import InterpolationMode
   
   def get_transform(opt, params=None, grayscale=False, method=Image.BICUBIC, convert=True):
   原81行
   
   def get_transform(opt, params=None, grayscale=False, method=InterpolationMode.BICUBIC, convert=True):
   改81行
   
   ```
