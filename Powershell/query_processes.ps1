$processList=get-process | Get-Unique
$procSamples = ((get-counter "\Process(*)\% Processor Time").countersamples) | sort -Property InstanceName
$cpuCores = (Get-WmiObject  Win32_Processor).numberofcores
$date=get-date
$i=0

Add-Content -path c:\windows\Logs\Process_Count.log -value "`r`n$date`r`n--Count of current processes--"

foreach ($process in $processList) {
    $pCount = (get-process $process.Name).count
    Add-Content -path c:\windows\Logs\Process_Count.log -value ("{0,-10} {1}" -f $pCount, $($process.Name))
    }

Add-Content -path c:\windows\Logs\Process_Count.log -value "`r`n--CPU usage of current processes--"

foreach ($procPerf in $procSamples) {
    Add-Content -path c:\windows\Logs\Process_Count.log -value ("{0,-10} {1}" -f [Math]::round(($procSamples[$i].CookedValue/$cpuCores),2).tostring(), $procSamples[$i].InstanceName)
    $i++
    }
   