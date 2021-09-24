FROM python:3
ADD calc_package /calc_package
ADD calculator.py /
RUN pip install -r requirements.txt
CMD ["python", "calculator.py"]
