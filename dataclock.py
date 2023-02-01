from datetime import date, datetime

import time
import os
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler


def tick():
    print("tick ! the time is : %s" % datetime.now())
    os.system("python Entrance.py")
    os.system("python split.py")
    os.system("python standoff2conll/standoff2conll.py /home/zzx/py/biobert-master/about/thepaper1.txt")
    os.system("python rmquotes.py")
    os.system("python run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --num_train_epochs=10.0 --data_dir=./about --output_dir=./ner_outputs")
    os.system("python run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --num_train_epochs=10.0 --data_dir=./about --output_dir=./ner_outputs_ch")
    os.system("python run_ner.py --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --num_train_epochs=10.0 --data_dir=./about --output_dir=./ner_outputs_ge")
    os.system("python biocodes/ner_detokenize.py --token_test_path=./ner_outputs/token_test.txt --label_test_path=./ner_outputs/label_test.txt --answer_path=./about/test.tsv --output_dir=./ner_outputs")
    os.system("python biocodes/ner_detokenize.py --token_test_path=./ner_outputs_ch/token_test.txt --label_test_path=./ner_outputs_ch/label_test.txt --answer_path=./about/test.tsv --output_dir=./ner_outputs_ch")
    os.system("python biocodes/ner_detokenize.py --token_test_path=./ner_outputs_ge/token_test.txt --label_test_path=./ner_outputs_ge/label_test.txt --answer_path=./about/test.tsv --output_dir=./ner_outputs_ge")
    os.system("python token2word.py --data_dir=./ner_outputs_ge --fileout_dir=about/genes.tsv ")
    os.system("python token2word.py --data_dir=./ner_outputs --fileout_dir=about/dines.tsv ")
    os.system("python token2word.py --data_dir=./ner_outputs_ch --fileout_dir=about/chnes.tsv ")
    os.system("python relationstract.py --nes1=about/dines.tsv --nes2=about/genes.tsv --nes1name=disease --nes2name=gene --paper=about/thepaper1.txt --fileout_dir=about/di_ge")
    os.system("python relationstract.py --nes1=about/chnes.tsv --nes2=about/dines.tsv --nes1name=chemical --nes2name=disease --paper=about/thepaper1.txt --fileout_dir=about/ch_di")
    os.system("python relationstract.py --nes1=about/chnes.tsv --nes2=about/genes.tsv --nes1name=chemical --nes2name=gene --paper=about/thepaper1.txt --fileout_dir=about/ch_ge")
    os.system("python relationstractgg.py --nes1=about/genes.tsv --nes1name=gene --paper=about/thepaper1.txt --fileout_dir=about/ge_ge")
    os.system("python run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./about/di_ge --output_dir=./re_outputs_1")
    os.system("python run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./about/ch_di --output_dir=./re_outputs_ch_di")
    os.system("python run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./about/ch_ge --output_dir=./re_outputs_ch_ge")
    os.system("python run_re.py --task_name=gad --do_train=false --do_eval=false --do_predict=true --vocab_file=./biobert_v1.1_pubmed/vocab.txt --bert_config_file=./biobert_v1.1_pubmed/bert_config.json --init_checkpoint=./biobert_v1.1_pubmed/model.ckpt-1000000 --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --do_lower_case=false --data_dir=./about/ge_ge --output_dir=./re_outputs_ge_ge")
    os.system("python tordf.py")
    os.system("python toneo.py")
if __name__ == "__main__":
    scheduler = BlockingScheduler()

    scheduler.add_job(tick, 'interval', days=1)

    scheduler.start()

    print("Press Ctrl + {0} to exit".format('Break' if os.name == 'nt' else 'C'))
    try:

        while True:
            time.sleep(600)
            print(f"sleep! - {datetime.now()}")

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Exit The Job !")