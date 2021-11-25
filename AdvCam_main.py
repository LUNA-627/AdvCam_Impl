import param_config as cfg
import argparse
import os
from AdvCam_attack import attack

parser = argparse.ArgumentParser()

parser.add_argument("--content", dest='content', nargs='?',
                    help="Path to the content image", default='stop-sign')
parser.add_argument("--style_content", dest='style_content', nargs='?',
                    help="Path to the style image", default='stop-sign')
parser.add_argument("--content_seg_path", dest='content_seg_path', nargs='?',
                    help="Path to the style segmentation", default='')
parser.add_argument("--style_seg_path", dest='style_seg_path', nargs='?',
                    help="Path to the style segmentation", default='')
parser.add_argument("--background_path", dest='background', nargs='?',
                    help="Path to init image", default='traffic')
parser.add_argument("--result_dir", dest='result_dir', nargs='?',
                    help='Path to save the results', default='stop-sign-lalala')
# Training Optimizer Options
parser.add_argument("--max_iter", dest='max_iter', nargs='?', type=int,
                    help='maximum image iteration', default=4000)
parser.add_argument("--learning_rate", dest='learning_rate', nargs='?', type=float,
                    help='learning rate for adam optimizer', default=1.0)
parser.add_argument("--save_iter", dest='save_iter', nargs='?', type=int,
                    help='save temporary result per iterations', default=50)

# Weight Options
parser.add_argument("--content_weight", dest='content_weight', nargs='?', type=float,
                    help="weight of content loss", default=5e0)
parser.add_argument("--style_weight", dest='style_weight', nargs='?', type=float,
                    help="weight of style loss", default=1e2)
parser.add_argument("--sm_weight", dest='sm_weight', nargs='?', type=float,
                    help="weight of total variational loss", default=1e-3)
parser.add_argument("--attack_weight", dest='attack_weight', nargs='?', type=float,
                    help="weight of attack loss", default=5e3)

# Attack Options
parser.add_argument("--targeted_attack", dest='targeted', nargs='?', type=int,
                    help="if True, targeted attack", default=1)
parser.add_argument("--target_label", dest='target', nargs='?', type=int,
                    help="The target label for target attack", default=184)
parser.add_argument("--true_label", dest='true_label', nargs='?', type=int,
                    help="The target label for target attack", default=8)

# test mode
parser.add_argument("--test_mode", dest='test_mode', nargs='?',
                    help="content/tv/affine/all", default='all')

# cpu/gpu
parser.add_argument("--p", dest='processor', nargs="?", type=int,
                    help="type 0 for cpu, type 1 for gpu, default 1", default=1)

args = parser.parse_args()

if args.processor == 0:
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

if __name__ == "__main__":
    args.target = 424
    config = cfg.Config(args)
    for content_path in config.get_contents():
        config.set_paths(args, content_path.split(os.path.sep)[-1])
        for num in (999, 1000):
            cfg.current_attack_weight = num
            attack()
        print("end all process")
