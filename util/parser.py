from darkflow.cli import cliHandler



def yolo_run(model,weights,video_file_or_camera='camera',use_gpu=True,save_results=False):

    output = "--model {} --load {} --demo {}".format(model,weights,video_file_or_camera)
    if use_gpu:
        output = output + (" --gpu 1.0")
    if save_results ==True:
        output = output + (" --saveVideo")

    _execute_yolo(output)



# execute clihandler via python
def _execute_yolo(commandstring):
    command = [""]+commandstring.split(" ")
    print ("executing command",command)
    cliHandler(command)
