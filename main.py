def argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', type=str, default="synthtext", help='input dataset - icdar15, synthtext')
    parser.add_argument('--dataset_path', type=str, default="", help='input dataset path')
    parser.add_argument('--batch_size', type=int, default=48, help='input batch size')
    parser.add_argument('--n_epochs', type=int, default=200, help='number of epochs to train for')
    parser.add_argument('--cuda', default=True, help='enables cuda')
    parser.add_argument('--gpu_id', type=int, default=0, help="ID of GPU on which to run network")
    parser.add_argument('--workers', type=int, default=6, help="num of dataloader workers")
    parser.add_argument('--pretrained', default="", help="path to pretrained model (to continue training)")
    parser.add_argument('--finetune', default=False, help="finetuning on different dataset")

    parser.add_argument('--display_interval', type=int, default=50, help='Interval to be displayed')
    parser.add_argument('--save_interval', type=int, default=5, help='Interval for model saving in terms of epoch num')
    parser.add_argument('--save_prefix', type=str, default="", help='prefix for filename to save state')
    parser.add_argument('--random_seed', type=int, default=5, help='random seed to reproduce experiment')
    parser.add_argument('--resume', type=bool, default=False, help='flag for resume')
    parser.add_argument('--resume_state', type=str, default="", help='saved state for resuming training')

    parser.add_argument('--lr', type=float, default=1e-2, help='learning rate for optimizer')
    parser.add_argument('--momentum', type=float, default=0.9, help='Momentum for SGD. default=0.9')
    parser.add_argument('--beta_1_adam', type=float, default=0.9, help='beta1 for adam. default=0.9')
    parser.add_argument('--adam', default=False, help='Whether to use adam (default is SGD)')
    parser.add_argument('--adadelta', default=False, help='Whether to use adadelta (default is SGD)')
    parser.add_argument('--step_interval', type=int, default=None, help='Interval to step down learning rate')
    parser.add_argument('--gamma', type=float, default=0.80, help='Factor to step down learning rate')
    parser.add_argument('--weight_decay', type=float, default=5e-4, help='Weight Decay Factor')
    parser.add_argument('--scheduler', type=bool, default=True, help='Cut LR by factor of gamma on val loss plateau')

    return parser.parse_args()


