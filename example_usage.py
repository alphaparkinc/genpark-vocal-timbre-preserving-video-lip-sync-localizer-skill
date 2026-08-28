from client import VocalTimbrePreservingVideoLipSyncLocalizerClient

def main():
    client = VocalTimbrePreservingVideoLipSyncLocalizerClient()
    res = client.localize_video_with_lip_sync('https://assets.genpark.ai/videos/product_launch.mp4', 'GERMAN')
    print('Video Localization Job: ' + res['localization_job_id'] + ' (Language: ' + res['target_language'] + ')')
    print('Timbre Similarity: ' + str(res['vocal_timbre_similarity_score_pct']) + '% | Lip Sync: ' + str(res['lip_sync_phoneme_alignment_accuracy_pct']) + '%')
    print('AV Desync: ' + str(res['audio_video_desync_ms']) + 'ms')
    print('Dubbed Video: ' + res['rendered_dubbed_video_url'])

if __name__ == '__main__':
    main()
