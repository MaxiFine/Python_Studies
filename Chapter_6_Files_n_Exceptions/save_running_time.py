# THIS PROGRAM SAVES A SEQUENCE OF VIDEO RUNNING
# TIMES TO THE VIDEO_TIMES.TXT FILE. IT DOES THE COMPUTATIONS
# AND DISPLAYS THE TOTAL VIDEO TIME OR SEQUENCE TIME


def main():  # THE MAIN FUNCTION WILL WRITE THE OUTPUT DATA

    # Get the number of videos in the project.
    num_videos = int(input("How many videos are in the project? "))

    # open the file hold the running times
    video_file = open('video_time.txt', 'w')

    # Getting each video's running time
    print("Enter the running times for each video")
    for count in range(1, num_videos + 1):
        run_time = float(input("Video #" + str(count) + ': '))
        video_file.write(str(run_time) + '\n')  # write data of run_time to video file

        # close file after writing
    video_file.close()

    output_runtime()    # CALLS FOR THE READ MODE AND DOES THE COMPUTATIONS


def output_runtime():   # READING THE OUTPUT FILE FOR OPERATIONS
    accumulator = 0  # to keep the total times

    read_file = open('video_time.txt', 'r')   # read the data of the
    # video file

    count = 0  # count for the number of videos entered to control
    # the loop

    print("Here are the running times for each video")

    # This function gets the data from the files and computes them
    for line in read_file:  # this code will read the data in the
        # video_times.txt file line by line.

        # converts each of the lines to numerical data type for computation
        run_time = float(line)

        count += 1

        # Display the times Entered by the year
        print("Video #", count, ': ', run_time, sep='')

        # Accumulate the running total of the video times
        accumulator += run_time

    # close file after mode operation
    read_file.close()

    # Display the total of the running times
    print("The total running time is", accumulator, 'seconds')


main()
