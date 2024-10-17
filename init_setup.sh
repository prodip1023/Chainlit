echo [$(date)]: "START"
echo [$(date)]: "creating a conda chainlit with python 3.10"
conda create --prefix ./chainlit python==3.10 -y
echo [$(date)]: "created conda chainlit"
source activate ./env
echo [$(date)]: "activated conda chainlit"
echo [$(date)]: "installing requirements"
pip install -r requirements.txt
echo[$(date)]: "insatlled all the requirement"
echo [$(date)]: "END"