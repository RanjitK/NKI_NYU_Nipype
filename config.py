# emacs =  -*- mode =  python; py-indent-offset =  4; indent-tabs-mode =  nil -*-
# vi =  set ft=python sts=4 ts=4 sw=4 et = 

"""
1. Distributed Processing Settings
    a) runOnGrid : options True/False or 0/1. Run On SGE Cluster/Grid
    b) qsubArgs : For use only when runOnGrid = True.

       -q QUEUE.q : The queue of nodes to use on the cluster/grid,
				    default is set to the queue of all nodes on the cluster(all.q).

    
       -pe A-B : Can Use with -q option. Specify the range of the number of slots to use on each node.
			  	 A is the lower bound on the range and B is the higher bound on the number of slots available

    c) num_cores: Use only when runOnGrid = False( or 0).
			      Specify the number of cores on a multiprocessor environment.
"""
runOnGrid = False
qsubArgs = '-q all.q'
numCores = 4


"""
2. Directory Setup
"""

"""
	a) Nipype Specifications
"""

"""
		Nipype Cache/Working/Debug Directory
		Nipype will dump Temporary outputs and workflow engine specific outputs to this directory. 
		Each User must set it. 
		It is recommended to delete this directory once the pipeline completes execution.

"""
workingDirectory = '/Users/ranjeet.khanuja/Documents/workspace/Scrub/development/working_dir_gp'

"""
    	Crash Log Directory
"""
crashLogDirectory = '/Users/ranjeet.khanuja/Documents/workspace/Scrub/development/working_dir4'

"""
	b) Data Specifications
"""

"""
    	Subject Data Directory and List
    	For Ex:
            If your data directory is 
            /data/projects/ADHD200/usable/0010001
            /data/projects/ADHD200/usable/0010002
    	subjectDirectory : '/data/projects/ADHD200/usable'
    	subjectList(Optional): Full path to the file that contains subject numbers, one per line.
		exclusionSubjectList(Optional) : File containing subjects which should be left unprocessed.
    	For Ex: subjectList : '/data/projects/ADHD200/docs/subjects.txt'

    	$ cat subjects.txt
    		0010001
    		0010002
		$ cat 

		Note: When subjectList is set to None, all the subjects in the subject directory, except the ones in
			  exclusionSubjectList are processed

"""
subjectDirectory = '/Users/ranjeet.khanuja/Desktop/data/replicate'
subjectList = '/Users/ranjeet.khanuja/Desktop/subjects.txt'
#subjectList = None
exclusionSubjectList = '/Users/ranjeet.khanuja/Desktop/exclude.txt'

"""
		Anatomical File Name and Location within Subject Directory
		Note: anatomicalFileName substituted into anatomicalFilePath 
			  Subject Number or subject names and anatomical file name automatically
			  substitute 1st %s and Last %s. This is done by the pipeline datasource. 
    	The user needs to set the directory structure

    	For Ex:
           /data/projects/ADHD200/
                        0010001/anat_1/mprage.nii.gz
                        0010001/anat_2/mprage.nii.gz
                        0010002/anat_1/mprage.nii.gz
                        0010002/anat_2/mprage.nii.gz
    
        set
        anatomicalFileName = 'mprage'
        
        anatomicalFilePath = '%s/*/%s.nii.gz'

        /sam/wave0/
                    sub3114/
                            session_1/anat_1/mprage.nii.gz
                            session_1/anat_2/mprage.nii.gz

                    sub3115/  
                            session_1/anat_1/mprage.nii.gz
        
    	anatomicalFileName = 'mprage'
        
    	anatomicalFilePath = '%s/*/*/%s.nii.gz'

"""
anatTemplate = '%s/session_1/anat/%s.nii.gz'
anatTemplateList = ['subject', 'mprage']
anatSessionFile = '/Users/ranjeet.khanuja/Desktop/session_anat.txt'

"""
	    anatLogFile: In case of multiple anatomical scans per subject.
					 Specify the name of the log file which indicates which single anatomical scan to process.

	    			anatLogFilePath: Specify the location of the log file relative to the subject directory location.
					The pipeline substitutes 1st %s with the subject number/name and the 2nd %s is the name of the log file. 
					The User needs to specify only the structure as per his analysis. 


	    Ex: /sam/wave1/sub8000/
                        anat_1/mprage.nii.gz
                        anat_2/mprage.nii.gz
                        logs/log.txt
	    anatLogFile = 'log.txt'
	    anatLogFilePath = '%s/*/%s'
    
"""
anatLogFile = 'log.txt'
anatLogFilePath = '%s/*/*/%s'



"""
		Functional File Name and Location within Subject Directory
		Note: functionalFileName substituted into functionalDirectorySetup template
"""
funcTemplate = '%s/session_1/%s/%s.nii.gz'
funcTemplateList = ['subject', 'session', 'rest']
funcSessionFile = '/Users/ranjeet.khanuja/Desktop/session.txt'


"""
    	Output Target Directory 
"""
sinkDirectory = '/Users/ranjeet.khanuja/Desktop/data/results'


"""
	c) Miscellaneous Specifications
"""


"""
    	Set FSL Directory (For Purposes of Template Selection)
"""
FSLDIR = '/usr/local/fsl/'


"""
    	Tissue Priors Directory
"""
priorDirectory = '/Users/ranjeet.khanuja/Documents/workspace/Scrub/development/tissuepriors'

"""
3. Optional Header and Timeseries Overrides
	nVols: Number of volumes in functional timeseries (defaults to image header specification)
	TR = time of repetition (defaults to image header specification)
    startIdx : starting time point(defaults to 0)
"""
startIdx = 0
stopIdx = 255
nVols = stopIdx - startIdx + 1
TR = 2.5


"""
4. Image Processing Specs
	NOTE: Specification of multiple parameters for any step indicates
		  execution of a unique processing path for each parameter from 
		  current step onward (e.g., fwhm = [4.5, 6]
		  will produce two unique output directories, one for 4.5 spatial smoothing and one for 6mm)
"""



"""
	a) MNI Template Resolution Specification For Registration
"""
standardResolution = '3mm'
MNI = 'MNI152'


"""
	b) Spatial Filter
		Lowpass 3D Gaussian Filter Kernel Specification in mm [FSL: fslmaths]
		note: Set to [] or 0 to skip spatial filtering
"""
fwhm = [6]

"""
    c) Set various thresholds for cerebral spinal fluid , white matter
    and gray matter mask generation during segmentation
"""
cerebralSpinalFluidThreshold = [0.4]
whiteMatterThreshold = [0.66]
grayMatterThreshold = [0.2]

"""
	d) Scrub data prior to derivate generation: In accord with Power et al. (2012)
	   Default value True/False or a list of True/False(if need both at the same time)
"""
scrubData = [False, True]

scrubbingThreshold = [0.5]


"""
	e) Nuisance Signal Correction
"""

"""
			Select Desired Approach:
				- Global mean signal regression
				- Compcor: 				   A component based noise correction method (CompCor)
										   for BOLD and perfusion based fMRI
										   Yashar Behzadia, Khaled Restoma, Joy Liaua, Thomas T. Liua, , 
										   Science Direct: Received 18 December 2006. Revised 23 April 2007.
										   Accepted 25 April 2007.
										   Available online 3 May 2007. 
				- White Matter
				- CSF regression (CSF)
				- GRAY Matter
				- First principal component regression:
										   Extracts the  principal components found in white matter and
    									   cerebral spinal fluid.  Algorithm based on:
										   Y. Behzadi, K. Restom, J. Liau, and T. T. Liu,
										   component based noise correction
										   method (CompCor) for BOLD and perfusion based fMRI.,
										   NeuroImage, vol. 37, no. 1,
										   pp. 90-101, Aug. 2007.
				- Motion Regression

"""
Corrections = [
[True, False, False, False, False, False, True],
[False, True, False, False, False, False, True]
]


"""
    f) For Compcor Use Only: Number of components to regress
"""
nComponents = [5, 6]


"""
    g) For Median Angle Correction Only: Target Angle (degrees)
	   Corrects the input file to a specified target angle in degrees.
       Algorithm based on:
       H. He and T. T. Liu, A geometric view of global signal confounds
       in resting-state functional MRI, NeuroImage, Sep. 2011.
"""
targetAngleDeg = [90, 60]


"""
	h) Temporal Filtering
	   Temporal Filter Specification in Hz performed after Nuisance Signal Correction
	   Note: Set to [] or 0 to skip high- or low-pass filter
"""
"""
		nuisanceHighPassFilter: Turn HighPassFilter ON(value : True/1), OFF(value : False/0)
		nuisanceLowPassFilter:  Turn LowPassFilter ON(value : True/1), OFF(value : False/0)
"""
nuisanceHighPassFilter = 1
nuisanceLowPassFilter = 1

"""
		highFreqLowCutoffNuisance: if HighPassFilter ON(value : True/1), then set this to a decimal value / List
		lowFreqHighCutoffNuisance: if LowPassFilter ON(value : True/1), then set this to a decimal value / List
		
		Note: Values for highFreqLowCutoffNuisance, lowFreqHighCutoffNuisance can be a list.
"""
nuisanceHighFreqLowCutOff = [0.01]
nuisanceLowFreqHighCutOff = [0.1]


"""
5. Derivative Specification
"""


"""
	a) Select Derivates:
		ALFF/fALFF, SCA, vmhc, reho,
		Unit (e.g., parcellation unit, mask) Time Series Extraction, Voxel TimeSeries Extraction, Vertices Extraction

		-ALFF/fALFF :
			  ALFF >> Zang, Y.F., He, Y., Zhu, C.Z., Cao, Q.J., Sui, M.Q., Liang, M., Tian, L.X., Jiang, T.Z., Wang, Y.F., 2007.
			  		  Altered baseline brain activity in children with ADHD
					  revealed by resting state functional MRI. Brain Dev
			  fALFF >> Zou, Q.H., Zhu, C.Z., Yang, Y., Zuo, X.N., Long, X.Y., Cao, Q.J., Wang, Y.F., Zang, Y.F., 2008.
					   An improved approach to detection of amplitude of low-frequency fluctuation (ALFF) for
					   resting state fMRI

		-SCA(seed based correlation analysis):
									   Biswal, B., Zerrin Yetkin, F., Haughton, V. M., & Hyde, J. S. (1995).
									   Functional connectivity in the motor cortex of resting human brain using echo-planar mri.
									   Magnetic Resonance in Medicine, 34(4), 537-541. doi:10.1002/mrm.1910340409

		-VMHC:
									   Zuo, X.-N., Kelly, C., Di Martino, A., Mennes, M., Margulies,
									   D. S., Bangaru, S., Grzadzinski, R., et al. (2010).
		 							   Growing together and growing apart: regional and sex differences in the
									   lifespan developmental trajectories of functional homotopy.
									   The Journal of neuroscience : the official journal of the
		 							   Society for Neuroscience, 30(45), 15034-43. doi:10.1523/JNEUROSCI.2612-10.2010

		-REHO:						   Regional homogeneity approach to fMRI data analysis, Zang 2004 NeuroImage.

		-Unit TimeSeries Extraction
		-Vertices Extraction
		-FSL Group Analysis: http://www.fmrib.ox.ac.uk/fsl/feat5/detail.html#higher
"""
derivatives = [False, False, False, False, False, False, True]


"""
	b) ALFF/fALFF Options
"""

"""
    		For ALFF/fALFF only
    			Notes: 1) This derivative is allergic to scrubbed data and thus will never use them.
           			   2) You need to specify both highPassFreqALFF and lowPassFreqALFF if you intend
              			  to use this derivative. The Default values are set below.
"""
highPassFreqALFF = [0.01]
lowPassFreqALFF = [0.1]



"""
	c) Seed-Based Correlation Analysis Options
"""

"""
    	For SCA use only
    	seedFile : specify full path to the seed list file.
    
		Each line of the seedFile contains full path to a seed.

"""
seedFile = '/Users/ranjeet.khanuja/Documents/workspace/Scrub/development/seed_list.txt'


"""
	d) Timeseries Extraction Options
"""

"""
			For Unit Timeseries Extraction Only
			Note: Definitions Directory should contain one subdirectory for each set of units
		  		  to be generated (e.g., Harvard-Oxford Atlas, AAL, Craddock, Dosenbach-160);
"""
unitDefinitionsDirectory = '/Users/ranjeet.khanuja/Desktop/data/parcelations'

# Output type: .csv, numPy
unitTSOutputs = [True, True]

"""
    		For Voxel Timeseries Extraction Only
			Note: Definitions Directory should contain one subdirectory for each
		  		  mask/mask set to be used to select voxels to be output; one output file / mask 
"""
voxelMasksDirectory = '/Users/ranjeet.khanuja/Desktop/data/masks'


# Output type: .csv, numPy
voxelTSOutputs = [False, True]

"""
    		For Vertices Timeseries Extraction Only
"""
# Output type: .csv, numPy
verticesTSOutputs = [False, True]
runSurfaceRegistraion = False
reconSubjectsDirectory = '/Users/ranjeet.khanuja/Desktop/data/recon_subject'


"""
	e) FSL Group Analysis
		Notes: 
			- Separate group analysis conducted for each derivative
			- Not applicable to time series extraction derivatives
"""
"""
    	List of one or more derivatives on which the group anlaysis is be run
    	As a default, some of derivatives which are generated from the pipleine have
    	been specified
"""
derivativeList = ['rest_Dickstein_accumbens_Z_fn2standard', 'sca_Z_fn2standard']

"""
		Specify Models Directory that contains one or more models to be executed per derivate
"""
modelsDirectory = '/Users/ranjeet.khanuja/Desktop/data2/models/'

"""
     	Templates for Group Analysis
     	Design Files
     	.con -> list of contrasts requested.
     	.fts -> list of F-tests requested.
     	.mat -> the actual values in the design matrix

     	model_name in the template_list will be fetch from  modelsDirectory above
"""
matTemplateList = ['model_name', 'model_name']
conTemplateList = ['model_name', 'model_name']
ftsTemplateList = ['model_name', 'model_name']
grpTemplateList = ['model_name', 'model_name']

mat = '%s/%s.mat'
con = '%s/%s.con'
fts = '%s/%s.fts'
grp = '%s/%s.grp'

"""
    	Derivative Template
    	The first argument is label which is actually the strategy name. The pipeline
    	automatically creates the lable-linkage file in the sym_links folder.
    	The second argument is derivative name. This will be fetched from 
    	the derivative list defined above
"""
subList='/Users/ranjeet.khanuja/Desktop/data2/subject_list.txt'
#dervTemplate = '/Users/ranjeet.khanuja/Desktop/data2/subjects/%s/%s/*/%s.nii.gz'
#labelFile = '/Users/ranjeet.khanuja/Desktop/label_linkage.txt'
dervTemplate = sinkDirectory+ '/sym_links/%s/%s/*/%s.nii.gz'
labelFile = sinkDirectory + '/sym_links/label_linkage.txt' 

dervTemplateList = ['label','derivative']

zThreshold = 2.3
pThreshold = 0.05
fTest = True
