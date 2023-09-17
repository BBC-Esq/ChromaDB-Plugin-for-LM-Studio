<a name="top"></a>

<div align="center">
  <h1>🚀 Supercharge your <a href="https://lmstudio.ai/">LM Studio</a>! with a Vector Database!</h1>
</div>

<!-- GPU Acceleration Support Table -->

<div align="center">
  <h4>⚡GPU Acceleration Support⚡
  <table>
    <thead>
      <tr>
        <th>GPU</th>
        <th>Windows</th>
        <th>Linux</th>
        <th>Requirements</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Nvidia</td>
        <td>✅</td>
        <td>✅</td>
        <td>CUDA 11.8 or 11.7</td>
      </tr>
      <tr>
        <td>AMD</td>
        <td>❌</td>
        <td>✅</td>
        <td>ROCm 5.4.2</td>
      </tr>
      <tr>
        <td>Apple/Metal</td>
        <td colspan="3" align="center"> ✅ </td>
      </tr>
    </tbody>
  </table></h4>
</div>

# Installation

> First, make sure you're running [Python 3.10+](https://www.python.org/downloads/release/python-31011/) and already have [Git](https://git-scm.com/downloads) installed.
<details>
  <summary>🪟 Windows</summary>
  
### Step 1 - GPU Acceleration Software
* Nvidia GPUs ➜ install [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
* AMD GPUs
    > Unfortuantely, PyTorch does not currently support AMD GPUs on Windows (only Linux).

### Step 2 - Obtain Repository
* Download the ZIP file containing the latest release for my repository.
* Unzip and place this folder anywhere you want on your computer.

### Step 3 - Virtual Environment
* Open the folder containing my repository files
* Create a command prompt and create a virtual environment with this command:
```
python -m venv .
```
* Then "activate" the virtual environment:
```
.\Scripts\activate
```

### Step 4 - Upgrade pip
```
python -m pip install --upgrade pip
```

### Step 5 - Install PyTorch
> If you're NOT using GPU acceleration use this instead: ```pip install torch torchvision torchaudio```
* Nvidia GPUs:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
> PyTorch does not currently support AMD GPUs on Windows (only Linux).

### Step 6 - Doublecheck GPU-Acceleration
```
python check_gpu.py
```

### Step 7 - Install Dependencies
```
pip install -r requirements.txt
```
</details>

<details>
  <summary>🐧 Linux</summary>

### Step 1 - GPU Acceleration Software
  * Nvidia GPUs ➜ install [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
  * AMD GPUs ➜ install ROCm version 5.4.2 according to the instructions [HERE](https://rocmdocs.amd.com/en/latest/deploy/linux/quick_start.html) and [HERE](https://rocmdocs.amd.com/en/latest/deploy/linux/index.html)

### Step 2 - Obtain Repository
* Download the ZIP file containing the latest release for my repository.  Inside the ZIP file is a folder holding my repository.  Unzip and place this folder anywhere you want on your computer.

### Step 3 - Virtual Environment
* Open the folder containing my repository files
* Create a command prompt and create a virtual environment with this command:
```
python -m venv .
```
* Then activate the virtual environment:
```
.\Scripts\activate
```

### Step 4 - Update Pip
```
python -m pip install --upgrade pip
```
### Step 5 - Install PyTorch
> If you're NOT using GPU acceleration: ```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu```
* For Nvidia GPUs:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
* For AMD GPUs:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2
```

### Step 6 - Doublecheck GPU-acceleration
```
python check_gpu.py
```
### Step 7 - Install Dependencies
```
pip install -r requirements.txt
```
</details>

<details>
  <summary>🍎 Apple</summary>

### Step 1 - GPU Acceleration Software
* All Macs with MacOS 12.3+ come with Metal/MPS support, which is the equivalent of CUDA and ROCm for Nvidia and AMD, respectively.
* However, you do need to have [Xcode Command Line Tools](https://www.makeuseof.com/install-xcode-command-line-tools/).

### Step 2 - Obtain Repository
* Download the ZIP file containing the latest release for my repository.  Inside the ZIP file is a folder holding my repository.  Unzip and place this folder anywhere you want on your computer.

### Step 3 - Virtual Environment
* Open the folder containing my repository files
* Create a terminal window and create a virtual environment with this command:
```
python3 -m venv .
```
* Then activate the virtual environment:
```
source bin/activate
```
### Step 5 - Update Pip
```
python3 -m pip install --upgrade pip
```
### Step 6 - Install PyTorch
```
pip3 install torch torchvision torchaudio
```
### Step 7 - Doublecheck Metal/MPS-acceleration
```
python3 check_gpu.py
```
### Step 8 - Install Dependencies
```
pip3 install -r requirements.txt
```
</details>

# Usage
<details>
  <summary>Instructions</summary>
  
### Step 1 - Virtual Environment
> For Macs the preferred command is ```python3 gui.py```
* Open a command prompt within my repository folder and activate the virtual environment:
```
python gui.py
```
### Step 2 - "Download Embedding Model"
* Choose a model to download using "Git."
    > You must wait until the download is complete AND unpacked before trying to create the database.

### Step 3 - "Select Embedding Model Directory"
* Selects the directory containing the model you want to use.
    > After you've downloaded more than one model you can test out different embedding models by clicking this again.

### Step 4 - "Choose Documents for Database"
* Select one or more files to include in the database.
> Current supported file types: pdf, docx, txt, json, enex, eml, msg, csv, xls, xlsx.<BR><BR>
> NOTE: You can always remove files from the "Docs_for_DB" folder, but you must recreate the vector database if you don't want them included in the new database.

### Step 5 - "Create Vector Database."
* You should see GPU usage spike.  After the spike, the program still needs to save the database to disk ("persist").  You must wait for this to complete before attempt to query the database.
    >You can look at the command prompt window to see exactly when the database is successfully "persisted."

### Step 6 - LM Studio
* Open LM Studio and load a model
    > Only Llama2-based models are currently supported.
* Click "Start Server" in the server tab.
* Within my program, type your question in the box and submit.
    >If you don't minimize LM Studio in this process you can actually see it being fed your question and the database results!
</details>

# Contact

All suggestions (positive and negative) are welcome.  "bbc@chintellalaw.com" or feel free to message me on the [LM Studio Discord Server](https://discord.gg/aPQfnNkxGC).

<div align="center">
  <img src="https://github.com/BBC-Esq/ChromaDB-Plugin-for-LM-Studio/raw/main/example.png" alt="Example Image">
</div>
