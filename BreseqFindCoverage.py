import argparse


parser = argparse.ArgumentParser(description='BreseqFindCoverage - A tool to find coverage of SNP of Breseq. '
                                             'Usage: python BreseqFindCoverage.py -i /file '
                                             'Output: /file/index.csv')
parser.add_argument('-i', '--input', type=str, help='Input pathway')

args = parser.parse_args()
outfh = open(args.input + '/index.csv', 'w')
infh = open(args.input + '/output/evidence/evidence.gd')
for line in infh:
    if len(line.split('\t')) > 6 and 'inside_cov' not in line:
        outfh.write(line.split('\t')[4] + '\t' + str(int(line.split('\tmajor_cov=')[1].split('/')[0]) + int(
            line.split('\tmajor_cov=')[1].split('\t')[0].split('/')[1])) + '\t' + str(
            int(line.split('\ttotal_cov=')[1].split('/')[0]) + int(
                line.split('\ttotal_cov=')[1].split('\n')[0].split('/')[1])) + '\t')
        if '\tmajor_frequency=1.000e+00' in line:
            outfh.write('100\n')
        else:
            outfh.write(str(float(line.split('\tmajor_frequency=')[1].split('e-01')[0]) * 10) + '\n')
infh.close()
outfh.close()