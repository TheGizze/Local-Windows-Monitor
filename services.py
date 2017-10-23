import subprocess


def get_all_services():

    #Runs Powershell command to get all installed services
    process = subprocess.Popen(["powershell", "Get-Service"], stdout=subprocess.PIPE)
    #captures the Powershell output to the result string
    result = process.communicate()[0]
    
    return result
