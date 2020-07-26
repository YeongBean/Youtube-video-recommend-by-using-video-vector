#!/bin/bash
cd ../../../mediapipe
. venv/bin/activate

/usr/local/bazel/2.0.0/lib/bazel/bin/bazel version && \
alias bazel='/usr/local/bazel/2.0.0/lib/bazel/bin/bazel'

python -m mediapipe.examples.desktop.youtube8m.generate_input_sequence_example \
  --path_to_input_video=/$1 \
  --clip_end_time_sec=$2

GLOG_logtostderr=1 bazel-bin/mediapipe/examples/desktop/youtube8m/extract_yt8m_features \
  --calculator_graph_config_file=mediapipe/graphs/youtube8m/feature_extraction.pbtxt \
  --input_side_packets=input_sequence_example=/tmp/mediapipe/metadata.pb  \
  --output_side_packets=output_sequence_example=/tmp/mediapipe/features.pb