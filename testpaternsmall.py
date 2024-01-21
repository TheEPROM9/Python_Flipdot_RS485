import numpy as np
from pyflipdot.sign import HanoverSign
from pyflipdot.pyflipdot import HanoverController
from serial import Serial
import time

# Array function for images
def eyes():
	image[2, 1] = True
	image[3, 1] = True
	image[4, 1] = True
	image[5, 1] = True
	
	image[2, 6] = True
	image[3, 6] = True
	image[4, 6] = True
	image[5, 6] = True
	
	image[1, 2] = True
	image[1, 3] = True
	image[1, 4] = True
	image[1, 5] = True
	
	image[6, 2] = True
	image[6, 3] = True
	image[6, 4] = True
	image[6, 5] = True
	
	image[3, 3] = True
	image[4, 3] = True
	image[3, 4] = True
	image[4, 4] = True
	
	image[4, 91] = True
	image[4, 92] = True
	image[3, 92] = True
	image[3, 91] = True
	
	image[2, 94] = True
	image[3, 94] = True
	image[4, 94] = True
	image[5, 94] = True
	
	image[2, 89] = True
	image[3, 89] = True
	image[4, 89] = True
	image[5, 89] = True
	
	image[1, 93] = True
	image[1, 92] = True
	image[1, 91] = True
	image[1, 90] = True
	
	image[6, 93] = True
	image[6, 92] = True
	image[6, 91] = True
	image[6, 90] = True
	
	# Write the image
	controller.draw_image(image)

def busface():
	image[0, 0] = False
	image[0, 1] = False
	image[0, 2] = False
	image[0, 3] = False
	image[0, 4] = False
	image[0, 5] = False
	image[0, 6] = False
	image[0, 7] = False
	image[0, 8] = False
	image[0, 9] = False
	image[0, 10] = False
	image[0, 11] = False
	image[0, 12] = False
	image[0, 13] = False
	image[0, 14] = False
	image[0, 15] = False
	image[0, 16] = False
	image[0, 17] = False
	image[0, 18] = False
	image[0, 19] = False
	image[0, 20] = False
	image[0, 21] = False
	image[0, 22] = False
	image[0, 23] = False
	image[0, 24] = False
	image[0, 25] = False
	image[0, 26] = False
	image[0, 27] = False
	image[0, 28] = False
	image[0, 29] = False
	image[0, 30] = False
	image[0, 31] = False
	image[0, 32] = False
	image[0, 33] = False
	image[0, 34] = False
	image[0, 35] = False
	image[0, 36] = False
	image[0, 37] = False
	image[0, 38] = False
	image[0, 39] = False
	image[0, 40] = False
	image[0, 41] = False
	image[0, 42] = False
	image[0, 43] = False
	image[0, 44] = False
	image[0, 45] = False
	image[0, 46] = False
	image[0, 47] = False
	image[0, 48] = False
	image[0, 49] = False
	image[0, 50] = False
	image[0, 51] = False
	image[0, 52] = False
	image[0, 53] = False
	image[0, 54] = False
	image[0, 55] = False
	image[0, 56] = False
	image[0, 57] = False
	image[0, 58] = False
	image[0, 59] = False
	image[0, 60] = False
	image[0, 61] = False
	image[0, 62] = False
	image[0, 63] = False
	image[0, 64] = False
	image[0, 65] = False
	image[0, 66] = False
	image[0, 67] = False
	image[0, 68] = False
	image[0, 69] = False
	image[0, 70] = False
	image[0, 71] = False
	image[0, 72] = False
	image[0, 73] = False
	image[0, 74] = False
	image[0, 75] = False
	image[0, 76] = False
	image[0, 77] = False
	image[0, 78] = False
	image[0, 79] = False
	image[0, 80] = False
	image[0, 81] = False
	image[0, 82] = False
	image[0, 83] = False
	image[0, 84] = True
	image[0, 85] = True
	image[0, 86] = True
	image[0, 87] = True
	image[0, 88] = True
	image[0, 89] = True
	image[0, 90] = True
	image[0, 91] = True
	image[0, 92] = False
	image[0, 93] = False
	image[0, 94] = False
	image[0, 95] = False
	image[1, 0] = False
	image[1, 1] = False
	image[1, 2] = False
	image[1, 3] = False
	image[1, 4] = False
	image[1, 5] = True
	image[1, 6] = True
	image[1, 7] = True
	image[1, 8] = True
	image[1, 9] = True
	image[1, 10] = False
	image[1, 11] = False
	image[1, 12] = False
	image[1, 13] = False
	image[1, 14] = False
	image[1, 15] = False
	image[1, 16] = False
	image[1, 17] = False
	image[1, 18] = False
	image[1, 19] = False
	image[1, 20] = False
	image[1, 21] = False
	image[1, 22] = False
	image[1, 23] = False
	image[1, 24] = False
	image[1, 25] = False
	image[1, 26] = False
	image[1, 27] = False
	image[1, 28] = False
	image[1, 29] = False
	image[1, 30] = False
	image[1, 31] = False
	image[1, 32] = False
	image[1, 33] = False
	image[1, 34] = False
	image[1, 35] = False
	image[1, 36] = False
	image[1, 37] = False
	image[1, 38] = False
	image[1, 39] = False
	image[1, 40] = False
	image[1, 41] = False
	image[1, 42] = False
	image[1, 43] = False
	image[1, 44] = True
	image[1, 45] = False
	image[1, 46] = False
	image[1, 47] = True
	image[1, 48] = False
	image[1, 49] = False
	image[1, 50] = False
	image[1, 51] = False
	image[1, 52] = False
	image[1, 53] = False
	image[1, 54] = False
	image[1, 55] = False
	image[1, 56] = False
	image[1, 57] = False
	image[1, 58] = False
	image[1, 59] = False
	image[1, 60] = False
	image[1, 61] = False
	image[1, 62] = False
	image[1, 63] = False
	image[1, 64] = False
	image[1, 65] = False
	image[1, 66] = False
	image[1, 67] = False
	image[1, 68] = False
	image[1, 69] = False
	image[1, 70] = False
	image[1, 71] = False
	image[1, 72] = False
	image[1, 73] = False
	image[1, 74] = False
	image[1, 75] = False
	image[1, 76] = False
	image[1, 77] = False
	image[1, 78] = False
	image[1, 79] = False
	image[1, 80] = False
	image[1, 81] = False
	image[1, 82] = False
	image[1, 83] = True
	image[1, 84] = True
	image[1, 85] = False
	image[1, 86] = False
	image[1, 87] = False
	image[1, 88] = False
	image[1, 89] = False
	image[1, 90] = False
	image[1, 91] = True
	image[1, 92] = True
	image[1, 93] = False
	image[1, 94] = False
	image[1, 95] = False
	image[2, 0] = False
	image[2, 1] = False
	image[2, 2] = False
	image[2, 3] = False
	image[2, 4] = True
	image[2, 5] = True
	image[2, 6] = False
	image[2, 7] = False
	image[2, 8] = False
	image[2, 9] = True
	image[2, 10] = True
	image[2, 11] = True
	image[2, 12] = True
	image[2, 13] = False
	image[2, 14] = False
	image[2, 15] = False
	image[2, 16] = False
	image[2, 17] = False
	image[2, 18] = False
	image[2, 19] = False
	image[2, 20] = False
	image[2, 21] = False
	image[2, 22] = False
	image[2, 23] = False
	image[2, 24] = False
	image[2, 25] = False
	image[2, 26] = False
	image[2, 27] = False
	image[2, 28] = False
	image[2, 29] = False
	image[2, 30] = False
	image[2, 31] = False
	image[2, 32] = False
	image[2, 33] = False
	image[2, 34] = False
	image[2, 35] = False
	image[2, 36] = False
	image[2, 37] = False
	image[2, 38] = False
	image[2, 39] = False
	image[2, 40] = False
	image[2, 41] = False
	image[2, 42] = False
	image[2, 43] = False
	image[2, 44] = True
	image[2, 45] = False
	image[2, 46] = False
	image[2, 47] = True
	image[2, 48] = False
	image[2, 49] = False
	image[2, 50] = False
	image[2, 51] = False
	image[2, 52] = False
	image[2, 53] = False
	image[2, 54] = False
	image[2, 55] = False
	image[2, 56] = False
	image[2, 57] = False
	image[2, 58] = False
	image[2, 59] = False
	image[2, 60] = False
	image[2, 61] = False
	image[2, 62] = False
	image[2, 63] = False
	image[2, 64] = False
	image[2, 65] = False
	image[2, 66] = False
	image[2, 67] = False
	image[2, 68] = False
	image[2, 69] = False
	image[2, 70] = False
	image[2, 71] = False
	image[2, 72] = False
	image[2, 73] = False
	image[2, 74] = False
	image[2, 75] = False
	image[2, 76] = False
	image[2, 77] = False
	image[2, 78] = False
	image[2, 79] = False
	image[2, 80] = False
	image[2, 81] = False
	image[2, 82] = False
	image[2, 83] = True
	image[2, 84] = False
	image[2, 85] = False
	image[2, 86] = False
	image[2, 87] = False
	image[2, 88] = False
	image[2, 89] = False
	image[2, 90] = False
	image[2, 91] = False
	image[2, 92] = True
	image[2, 93] = False
	image[2, 94] = False
	image[2, 95] = False
	image[3, 0] = False
	image[3, 1] = False
	image[3, 2] = False
	image[3, 3] = True
	image[3, 4] = True
	image[3, 5] = False
	image[3, 6] = False
	image[3, 7] = False
	image[3, 8] = False
	image[3, 9] = False
	image[3, 10] = False
	image[3, 11] = False
	image[3, 12] = True
	image[3, 13] = False
	image[3, 14] = False
	image[3, 15] = True
	image[3, 16] = False
	image[3, 17] = False
	image[3, 18] = False
	image[3, 19] = False
	image[3, 20] = False
	image[3, 21] = False
	image[3, 22] = False
	image[3, 23] = False
	image[3, 24] = False
	image[3, 25] = False
	image[3, 26] = False
	image[3, 27] = False
	image[3, 28] = False
	image[3, 29] = False
	image[3, 30] = False
	image[3, 31] = False
	image[3, 32] = False
	image[3, 33] = False
	image[3, 34] = False
	image[3, 35] = False
	image[3, 36] = False
	image[3, 37] = False
	image[3, 38] = False
	image[3, 39] = False
	image[3, 40] = False
	image[3, 41] = False
	image[3, 42] = False
	image[3, 43] = False
	image[3, 44] = True
	image[3, 45] = False
	image[3, 46] = False
	image[3, 47] = True
	image[3, 48] = False
	image[3, 49] = False
	image[3, 50] = False
	image[3, 51] = False
	image[3, 52] = False
	image[3, 53] = False
	image[3, 54] = False
	image[3, 55] = False
	image[3, 56] = False
	image[3, 57] = False
	image[3, 58] = False
	image[3, 59] = False
	image[3, 60] = False
	image[3, 61] = False
	image[3, 62] = False
	image[3, 63] = False
	image[3, 64] = False
	image[3, 65] = False
	image[3, 66] = False
	image[3, 67] = False
	image[3, 68] = False
	image[3, 69] = False
	image[3, 70] = False
	image[3, 71] = False
	image[3, 72] = False
	image[3, 73] = False
	image[3, 74] = False
	image[3, 75] = False
	image[3, 76] = False
	image[3, 77] = False
	image[3, 78] = False
	image[3, 79] = True
	image[3, 80] = True
	image[3, 81] = False
	image[3, 82] = False
	image[3, 83] = True
	image[3, 84] = False
	image[3, 85] = False
	image[3, 86] = False
	image[3, 87] = False
	image[3, 88] = False
	image[3, 89] = False
	image[3, 90] = False
	image[3, 91] = False
	image[3, 92] = True
	image[3, 93] = True
	image[3, 94] = False
	image[3, 95] = False
	image[4, 0] = False
	image[4, 1] = False
	image[4, 2] = False
	image[4, 3] = True
	image[4, 4] = False
	image[4, 5] = False
	image[4, 6] = False
	image[4, 7] = True
	image[4, 8] = False
	image[4, 9] = False
	image[4, 10] = False
	image[4, 11] = False
	image[4, 12] = True
	image[4, 13] = False
	image[4, 14] = False
	image[4, 15] = True
	image[4, 16] = True
	image[4, 17] = False
	image[4, 18] = False
	image[4, 19] = False
	image[4, 20] = False
	image[4, 21] = False
	image[4, 22] = False
	image[4, 23] = False
	image[4, 24] = False
	image[4, 25] = False
	image[4, 26] = False
	image[4, 27] = False
	image[4, 28] = False
	image[4, 29] = False
	image[4, 30] = False
	image[4, 31] = False
	image[4, 32] = False
	image[4, 33] = False
	image[4, 34] = False
	image[4, 35] = False
	image[4, 36] = False
	image[4, 37] = False
	image[4, 38] = False
	image[4, 39] = False
	image[4, 40] = False
	image[4, 41] = False
	image[4, 42] = False
	image[4, 43] = False
	image[4, 44] = False
	image[4, 45] = False
	image[4, 46] = False
	image[4, 47] = False
	image[4, 48] = False
	image[4, 49] = False
	image[4, 50] = False
	image[4, 51] = False
	image[4, 52] = False
	image[4, 53] = False
	image[4, 54] = False
	image[4, 55] = False
	image[4, 56] = False
	image[4, 57] = False
	image[4, 58] = False
	image[4, 59] = False
	image[4, 60] = False
	image[4, 61] = False
	image[4, 62] = False
	image[4, 63] = False
	image[4, 64] = False
	image[4, 65] = False
	image[4, 66] = False
	image[4, 67] = False
	image[4, 68] = False
	image[4, 69] = False
	image[4, 70] = False
	image[4, 71] = False
	image[4, 72] = False
	image[4, 73] = False
	image[4, 74] = False
	image[4, 75] = False
	image[4, 76] = False
	image[4, 77] = True
	image[4, 78] = True
	image[4, 79] = True
	image[4, 80] = False
	image[4, 81] = False
	image[4, 82] = False
	image[4, 83] = True
	image[4, 84] = False
	image[4, 85] = False
	image[4, 86] = False
	image[4, 87] = False
	image[4, 88] = True
	image[4, 89] = False
	image[4, 90] = False
	image[4, 91] = False
	image[4, 92] = False
	image[4, 93] = True
	image[4, 94] = False
	image[4, 95] = False
	image[5, 0] = False
	image[5, 1] = False
	image[5, 2] = False
	image[5, 3] = True
	image[5, 4] = False
	image[5, 5] = False
	image[5, 6] = False
	image[5, 7] = False
	image[5, 8] = False
	image[5, 9] = False
	image[5, 10] = True
	image[5, 11] = True
	image[5, 12] = True
	image[5, 13] = False
	image[5, 14] = False
	image[5, 15] = False
	image[5, 16] = True
	image[5, 17] = True
	image[5, 18] = False
	image[5, 19] = False
	image[5, 20] = False
	image[5, 21] = False
	image[5, 22] = False
	image[5, 23] = False
	image[5, 24] = False
	image[5, 25] = False
	image[5, 26] = False
	image[5, 27] = False
	image[5, 28] = False
	image[5, 29] = False
	image[5, 30] = False
	image[5, 31] = False
	image[5, 32] = False
	image[5, 33] = False
	image[5, 34] = False
	image[5, 35] = False
	image[5, 36] = False
	image[5, 37] = False
	image[5, 38] = False
	image[5, 39] = False
	image[5, 40] = False
	image[5, 41] = False
	image[5, 42] = False
	image[5, 43] = False
	image[5, 44] = False
	image[5, 45] = False
	image[5, 46] = False
	image[5, 47] = False
	image[5, 48] = False
	image[5, 49] = False
	image[5, 50] = False
	image[5, 51] = False
	image[5, 52] = False
	image[5, 53] = False
	image[5, 54] = False
	image[5, 55] = False
	image[5, 56] = False
	image[5, 57] = False
	image[5, 58] = False
	image[5, 59] = False
	image[5, 60] = False
	image[5, 61] = False
	image[5, 62] = False
	image[5, 63] = False
	image[5, 64] = False
	image[5, 65] = False
	image[5, 66] = False
	image[5, 67] = False
	image[5, 68] = False
	image[5, 69] = False
	image[5, 70] = False
	image[5, 71] = False
	image[5, 72] = False
	image[5, 73] = False
	image[5, 74] = False
	image[5, 75] = False
	image[5, 76] = False
	image[5, 77] = True
	image[5, 78] = False
	image[5, 79] = False
	image[5, 80] = False
	image[5, 81] = False
	image[5, 82] = False
	image[5, 83] = True
	image[5, 84] = True
	image[5, 85] = False
	image[5, 86] = False
	image[5, 87] = False
	image[5, 88] = False
	image[5, 89] = False
	image[5, 90] = False
	image[5, 91] = False
	image[5, 92] = True
	image[5, 93] = True
	image[5, 94] = False
	image[5, 95] = False
	image[6, 0] = False
	image[6, 1] = False
	image[6, 2] = False
	image[6, 3] = True
	image[6, 4] = True
	image[6, 5] = True
	image[6, 6] = True
	image[6, 7] = True
	image[6, 8] = True
	image[6, 9] = True
	image[6, 10] = True
	image[6, 11] = False
	image[6, 12] = False
	image[6, 13] = False
	image[6, 14] = False
	image[6, 15] = False
	image[6, 16] = False
	image[6, 17] = True
	image[6, 18] = True
	image[6, 19] = True
	image[6, 20] = True
	image[6, 21] = True
	image[6, 22] = True
	image[6, 23] = True
	image[6, 24] = True
	image[6, 25] = True
	image[6, 26] = True
	image[6, 27] = True
	image[6, 28] = True
	image[6, 29] = True
	image[6, 30] = True
	image[6, 31] = True
	image[6, 32] = False
	image[6, 33] = False
	image[6, 34] = False
	image[6, 35] = False
	image[6, 36] = False
	image[6, 37] = False
	image[6, 38] = False
	image[6, 39] = False
	image[6, 40] = False
	image[6, 41] = False
	image[6, 42] = False
	image[6, 43] = False
	image[6, 44] = True
	image[6, 45] = True
	image[6, 46] = True
	image[6, 47] = True
	image[6, 48] = True
	image[6, 49] = True
	image[6, 50] = True
	image[6, 51] = True
	image[6, 52] = True
	image[6, 53] = True
	image[6, 54] = True
	image[6, 55] = True
	image[6, 56] = True
	image[6, 57] = True
	image[6, 58] = True
	image[6, 59] = True
	image[6, 60] = True
	image[6, 61] = True
	image[6, 62] = False
	image[6, 63] = False
	image[6, 64] = False
	image[6, 65] = False
	image[6, 66] = False
	image[6, 67] = True
	image[6, 68] = True
	image[6, 69] = True
	image[6, 70] = True
	image[6, 71] = True
	image[6, 72] = True
	image[6, 73] = True
	image[6, 74] = True
	image[6, 75] = True
	image[6, 76] = True
	image[6, 77] = True
	image[6, 78] = False
	image[6, 79] = False
	image[6, 80] = False
	image[6, 81] = False
	image[6, 82] = False
	image[6, 83] = False
	image[6, 84] = True
	image[6, 85] = True
	image[6, 86] = True
	image[6, 87] = False
	image[6, 88] = False
	image[6, 89] = False
	image[6, 90] = False
	image[6, 91] = True
	image[6, 92] = True
	image[6, 93] = False
	image[6, 94] = False
	image[6, 95] = False
	image[7, 0] = False
	image[7, 1] = False
	image[7, 2] = False
	image[7, 3] = False
	image[7, 4] = False
	image[7, 5] = False
	image[7, 6] = False
	image[7, 7] = False
	image[7, 8] = False
	image[7, 9] = False
	image[7, 10] = False
	image[7, 11] = False
	image[7, 12] = False
	image[7, 13] = False
	image[7, 14] = False
	image[7, 15] = False
	image[7, 16] = False
	image[7, 17] = False
	image[7, 18] = False
	image[7, 19] = False
	image[7, 20] = False
	image[7, 21] = False
	image[7, 22] = False
	image[7, 23] = False
	image[7, 24] = False
	image[7, 25] = False
	image[7, 26] = False
	image[7, 27] = False
	image[7, 28] = False
	image[7, 29] = False
	image[7, 30] = False
	image[7, 31] = False
	image[7, 32] = True
	image[7, 33] = True
	image[7, 34] = True
	image[7, 35] = True
	image[7, 36] = True
	image[7, 37] = True
	image[7, 38] = True
	image[7, 39] = True
	image[7, 40] = True
	image[7, 41] = True
	image[7, 42] = True
	image[7, 43] = True
	image[7, 44] = True
	image[7, 45] = False
	image[7, 46] = False
	image[7, 47] = False
	image[7, 48] = False
	image[7, 49] = False
	image[7, 50] = False
	image[7, 51] = False
	image[7, 52] = False
	image[7, 53] = False
	image[7, 54] = False
	image[7, 55] = False
	image[7, 56] = False
	image[7, 57] = False
	image[7, 58] = False
	image[7, 59] = False
	image[7, 60] = False
	image[7, 61] = True
	image[7, 62] = True
	image[7, 63] = True
	image[7, 64] = True
	image[7, 65] = True
	image[7, 66] = True
	image[7, 67] = True
	image[7, 68] = False
	image[7, 69] = False
	image[7, 70] = False
	image[7, 71] = False
	image[7, 72] = False
	image[7, 73] = False
	image[7, 74] = False
	image[7, 75] = False
	image[7, 76] = False
	image[7, 77] = False
	image[7, 78] = False
	image[7, 79] = False
	image[7, 80] = False
	image[7, 81] = False
	image[7, 82] = False
	image[7, 83] = False
	image[7, 84] = False
	image[7, 85] = True
	image[7, 86] = True
	image[7, 87] = True
	image[7, 88] = True
	image[7, 89] = True
	image[7, 90] = True
	image[7, 91] = True
	image[7, 92] = False
	image[7, 93] = False
	image[7, 94] = False
	image[7, 95] = False

	# Write the image
	controller.draw_image(image)

# Create a serial port (update with port name on your system)
ser = Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0')

# Create a controller
controller = HanoverController(ser)

# Add a sign
# Note: The sign's address is set via it's potentiometer
#sign = HanoverSign(address=1, width=96, height=8)
sign = HanoverSign(address=1, width=96, height=8)
controller.add_sign('dev', sign)

# Create a 'checkerboard' image
image = sign.create_image()
# [ x , y ]
# : = Solid Line
# ; = Every Other LED

# Forloop runs the arrays in an sudo animation
for x in range(10):
	eyes()
	time.sleep(3)
	busface()
	time.sleep(3)

#eyes()

#busface()