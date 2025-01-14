import jiwer
import os

def calculate_wer_cer(pred_text, true_text):
    """
    Calculate the Word Error Rate (WER) and Character Error Rate (CER) between
    the predicted text and the ground truth text.

    Args:
    pred_text (str): Path to the file containing the predicted text.
    true_text (str): Path to the file containing the ground truth text.

    Returns:
    tuple: WER and CER as floats.
    """
    with open(pred_text, 'r', encoding='utf-8') as f:
        predicted = f.read().strip()
    
    with open(true_text, 'r', encoding='utf-8') as f:
        ground_truth = f.read().strip()

    wer = jiwer.wer(ground_truth, predicted)
    cer = jiwer.cer(ground_truth, predicted)
    return wer, cer

def evaluate_all(output_folder, truth_folder):
    """
    Calculate and print the WER and CER for each pair of files in the output and truth folders.

    Args:
    output_folder (str): Path to the folder containing the predicted text files.
    truth_folder (str): Path to the folder containing the ground truth text files.
    """
    output_files = [f for f in os.listdir(output_folder) if f.endswith('.txt')]
    
    wer_list = []
    cer_list = []

    for output_file in output_files:
        output_path = os.path.join(output_folder, output_file)
        truth_path = os.path.join(truth_folder, output_file)

        if os.path.exists(truth_path):
            wer, cer = calculate_wer_cer(output_path, truth_path)
            wer_list.append(wer)
            cer_list.append(cer)
            print(f'{output_file} - WER: {wer:.4f}, CER: {cer:.4f}')
        else:
            print(f'Ground truth file for {output_file} not found.')

    if wer_list and cer_list:
        avg_wer = sum(wer_list) / len(wer_list)
        avg_cer = sum(cer_list) / len(cer_list)
        print(f'\nAverage WER: {avg_wer:.4f}')
        print(f'Average CER: {avg_cer:.4f}')
    else:
        print('No valid pairs of output and ground truth files found.')

if __name__ == "__main__":
    output_folder = 'C:\\Users\\kenan\\Desktop\\Arabic-OCR-master\\src\\output\\text'  # Path to the output folder
    truth_folder = 'C:\\Users\\kenan\\Desktop\\Arabic-OCR-master\\src\\truth'  # Path to the ground truth folder
    evaluate_all(output_folder, truth_folder)
