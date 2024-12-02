$Comliance = "YES"

$fixedDisks = Get - Disk | Where - Object
{$_.BusType - ne
'USB'}

$driveLetters = foreach($disk in $fixedDisks)
{
    Get - Partition - DiskNumber $disk.DiskNumber | Where - Object
{$_.Type - eq
"Basic"} | Select - ExpandProperty
DriveLetter
}

$nobitlocker = foreach($letter in $driveLetters)
{
    Get - BitLockerVolume - MountPoint $letter | Where - Object
{$_.ProtectionStatus - eq
"off"} | select - ExpandProperty
MountPoint

}

If($nobitlocker)
{
$Comliance = "NO"
}

$Comliance