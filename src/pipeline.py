from sklearn.pipeline import Pipeline
from custom_transformers.split_silence_transformer import SplitSilenceTransformer
from custom_transformers.mfcc_transformer import MfccTransformer
from custom_transformers.expander_transformer import ExpanderTransformer
from custom_transformers.label_encoder_transformer import LabelEncoderTransformer
from custom_transformers.standard_scaler import StandardScalerTransformer


def make_pipeline(sampling_rating,
                  threshold_percentage,
                  min_silence_duration,
                  frame_length_energy,
                  hop_length,
                  n_mfcc, 
                  segment_duration,
                  segment_overlap):
    pipeline = Pipeline(
        [
            ("split_silence_transformer", SplitSilenceTransformer(
                variables=['audio', 'label'],
                sampling_rating=sampling_rating,
                threshold_percentage=threshold_percentage,
                min_silence_duration=min_silence_duration,
                frame_length_energy=frame_length_energy,
                hop_length=hop_length)),
            
            ("mfcc_transformer", MfccTransformer(variables=["audio", "label"],
                sampling_rating=sampling_rating, 
                n_mfcc=n_mfcc,
                duration=segment_duration,
                overlap=segment_overlap)),
            
            ("expander_transformer", ExpanderTransformer(n_mfcc=n_mfcc, columns_to_remain=["label"])),

            ("label_encoder", LabelEncoderTransformer(variable='label')),
            
            ("scaler", StandardScalerTransformer(n_mfccs=n_mfcc))
        ]
    )
    return pipeline
