def getInput():
    n = int(input())
    gbm = str(input())

    return n, gbm

def formatDate(gbm_s):
    # ruleset
    MX_LEN = 2
    MX_DAY = 31
    MM_DAY = 1

    digits_to_analyze = []

    digits_to_analyze = 



def formatMonth(gbm_s):
    pass

def formatYear(gbm_s):
    pass

def Solution():
    n, gbm = getInput()
    gbm_spliced = gbm.replace('-', '')

    L_DAY = formatDate(gbm_s=gbm_spliced)
    L_MONTH = formatMonth(gbm_s=gbm_spliced)
    L_YEAR = formatYear(gbm_s=gbm_spliced)

Solution()