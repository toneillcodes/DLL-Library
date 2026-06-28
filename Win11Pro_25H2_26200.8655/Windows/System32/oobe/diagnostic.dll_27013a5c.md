# Binary Specification: diagnostic.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oobe\diagnostic.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `27013a5ce7073139d7d5875e415018c3f3482a4dfaa303971ecf32b4b2104f8b`
* **Total Exported Functions:** 166

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `??0CAccessWMI@@QEAA@AEBV0@@Z` | `0x2370` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??4CAccessWMI@@QEAAAEAV0@AEBV0@@Z` | `0x23C0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `?ResetWmiClassName@CAccessWMI@@IEAAXPEBG@Z` | `0x24A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CAccessWMI@@IEAA@PEBG@Z` | `0x24B0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??1CAccessWMI@@MEAA@XZ` | `0x26D0` | 35 | UnwindData |  |
| 67 | `?ConnectWMI@CAccessWMI@@IEAA_NXZ` | `0x2870` | 518 | UnwindData |  |
| 77 | `?DisconnectWMI@CAccessWMI@@IEAAXXZ` | `0x2AB0` | 90 | UnwindData |  |
| 81 | `?ExecQuery@CAccessWMI@@IEAA_NXZ` | `0x2B10` | 388 | UnwindData |  |
| 82 | `?FetchInfo@CAccessWMI@@IEAA_NPEBGAEAK@Z` | `0x2CA0` | 328 | UnwindData |  |
| 83 | `?FetchInfo@CAccessWMI@@IEAA_NPEBGAEA_J@Z` | `0x2DF0` | 225 | UnwindData |  |
| 84 | `?FetchInfo@CAccessWMI@@IEAA_NPEBGPEAG_K@Z` | `0x2EE0` | 330 | UnwindData |  |
| 128 | `?LogErrorMessage@CAccessWMI@@IEAAXPEBGKW4tagLOG_SETUPLOG_SEVERITY@@@Z` | `0x33C0` | 208 | UnwindData |  |
| 131 | `?LogFetchInfoError@CAccessWMI@@AEAAXPEBGI@Z` | `0x34A0` | 167 | UnwindData |  |
| 7 | `??0CMoboAndProcInfo@@QEAA@AEBV0@@Z` | `0x3830` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CMoboAndProcInfo@@QEAA@XZ` | `0x38C0` | 279 | UnwindData |  |
| 27 | `??1CMoboAndProcInfo@@UEAA@XZ` | `0x39E0` | 35 | UnwindData |  |
| 42 | `??4CMoboAndProcInfo@@QEAAAEAV0@AEBV0@@Z` | `0x3A10` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `?GetAvailPhysRAM@CMoboAndProcInfo@@QEAAKXZ` | `0x3B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?GetNumberOfProcessors@CMoboAndProcInfo@@QEAAKXZ` | `0x3B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?GetProcAddressWidth@CMoboAndProcInfo@@QEAAKXZ` | `0x3B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?GetProcArchitecture@CMoboAndProcInfo@@QEAAKXZ` | `0x3B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `?GetProcFamily@CMoboAndProcInfo@@QEAAKXZ` | `0x3B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?GetProcStepping@CMoboAndProcInfo@@QEAAKXZ` | `0x3B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `?GetProcessorInfo@CMoboAndProcInfo@@AEAAXXZ` | `0x3B70` | 317 | UnwindData |  |
| 112 | `?GetProcessorSpeedInMHz@CMoboAndProcInfo@@QEAAKXZ` | `0x3CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?GetTotalPhysRAM@CMoboAndProcInfo@@QEAAKXZ` | `0x3CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CHardwareID@@QEAA@XZ` | `0x3CE0` | 400 | UnwindData |  |
| 25 | `??1CHardwareID@@QEAA@XZ` | `0x3E80` | 91 | UnwindData |  |
| 40 | `??4CHardwareID@@QEAAAEAV0@AEBV0@@Z` | `0x3EF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?DestroyArray@CHardwareID@@AEAAXPEAV?$CAtlArray@PEBGV?$CElementTraits@PEBG@ATL@@@ATL@@@Z` | `0x3F20` | 144 | UnwindData |  |
| 80 | `?EnumDevices@CHardwareID@@AEAAXXZ` | `0x3FC0` | 292 | UnwindData |  |
| 90 | `?GetCompatibleIds@CHardwareID@@QEAAPEAPEBGXZ` | `0x40F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?GetHardwareIds@CHardwareID@@QEAAPEAPEBGXZ` | `0x4100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?GetNumberOfCompatableIDs@CHardwareID@@QEAAKXZ` | `0x4110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `?GetNumberOfHardwareIds@CHardwareID@@QEAAKXZ` | `0x4120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?GetProperties@CHardwareID@@AEAAXKPEAXPEAU_SP_DEVINFO_DATA@@PEAV?$CAtlArray@PEBGV?$CElementTraits@PEBG@ATL@@@ATL@@@Z` | `0x4130` | 404 | UnwindData |  |
| 129 | `?LogErrorMessage@CHardwareID@@AEAAXPEBGK@Z` | `0x43F0` | 183 | UnwindData |  |
| 130 | `?LogErrorMessageGLE@CHardwareID@@AEAAXPEBGK@Z` | `0x44B0` | 170 | UnwindData |  |
| 4 | `??0CExistingOS@@QEAA@XZ` | `0x4560` | 406 | UnwindData |  |
| 10 | `??0CSqmDiagConsumer@@QEAA@AEBV0@@Z` | `0x4700` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0IDiagConsumer@@QEAA@AEBV0@@Z` | `0x4740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0IDiagConsumer@@QEAA@XZ` | `0x4740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0InstallData@@QEAA@AEBV0@@Z` | `0x4760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0MachineHardWare@@QEAA@AEBV0@@Z` | `0x4780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0NewSystem@@QEAA@AEBV0@@Z` | `0x47B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0OldSystem@@QEAA@AEBV0@@Z` | `0x47D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??1CExistingOS@@QEAA@XZ` | `0x47F0` | 137 | UnwindData |  |
| 30 | `??1IDiagConsumer@@UEAA@XZ` | `0x4880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??4CCountArray@@QEAAAEAV0@AEBV0@@Z` | `0x48A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??4CDiagConsumerAdaptorFactory@@QEAAAEAV0@$$QEAV0@@Z` | `0x48C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??4CDiagConsumerAdaptorFactory@@QEAAAEAV0@AEBV0@@Z` | `0x48C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??4IDiagConsumer@@QEAAAEAV0@AEBV0@@Z` | `0x48C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??4CExistingOS@@QEAAAEAV0@AEBV0@@Z` | `0x48D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??4CInstallSource@@QEAAAEAV0@AEBV0@@Z` | `0x4950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??4CNewOS@@QEAAAEAV0@AEBV0@@Z` | `0x4970` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??4CSqmDiagConsumer@@QEAAAEAV0@AEBV0@@Z` | `0x49F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??4InstallData@@QEAAAEAV0@AEBV0@@Z` | `0x4A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??4NewSystem@@QEAAAEAV0@AEBV0@@Z` | `0x4A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??4OldSystem@@QEAAAEAV0@AEBV0@@Z` | `0x4A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??4MachineHardWare@@QEAAAEAV0@AEBV0@@Z` | `0x4A50` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?DetectBranch@CExistingOS@@AEAAXXZ` | `0x4B90` | 794 | UnwindData |  |
| 91 | `?GetDeviceDword@CExistingOS@@QEAAKW4eDeviceDword@1@@Z` | `0x4EB0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `?GetDeviceString@CExistingOS@@QEAAPEBGW4eDeviceString@1@@Z` | `0x4F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?GetFailedInstallCount@CExistingOS@@QEAAKXZ` | `0x4FA0` | 797 | UnwindData |  |
| 106 | `?GetOEMInformation@CExistingOS@@AEAAXXZ` | `0x52D0` | 576 | UnwindData |  |
| 114 | `?GetSkuInfo@CExistingOS@@AEAAKPEAK@Z` | `0x5520` | 843 | UnwindData |  |
| 115 | `?GetSystemVersionDetails@CExistingOS@@AEAAXXZ` | `0x5880` | 404 | UnwindData |  |
| 144 | `?NumElements@CCountArray@@QEAAIXZ` | `0x5D40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0CNewOS@@QEAA@PEAU_BLACKBOARD@@@Z` | `0x5DC0` | 361 | UnwindData |  |
| 26 | `??1CInstallSource@@QEAA@XZ` | `0x5F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??1CNewOS@@QEAA@XZ` | `0x5F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?LogToFile@InstallData@@UEAAXXZ` | `0x5F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?LogToFile@NewSystem@@UEAAXXZ` | `0x5F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `?LogToFile@OldSystem@@UEAAXXZ` | `0x5F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?FillWithBranchDetails@CNewOS@@AEAAXPEAG@Z` | `0x5F40` | 170 | UnwindData |  |
| 86 | `?FillWithBuildDate@CNewOS@@AEAAXPEAG@Z` | `0x5FF0` | 135 | UnwindData |  |
| 87 | `?FillWithVersionAndBuildProperties@CNewOS@@AEAAXPEAG@Z` | `0x6080` | 184 | UnwindData |  |
| 88 | `?FindFilePathInAppDir@CNewOS@@AEAA_NPEAGIPEBG@Z` | `0x6140` | 419 | UnwindData |  |
| 93 | `?GetDeviceDword@CNewOS@@QEAAKW4eDeviceDword@1@@Z` | `0x62F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `?GetDeviceString@CNewOS@@QEAAPEBGW4eDeviceString@1@@Z` | `0x6370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?GetEdition@CNewOS@@SAPEBGPEAU_BLACKBOARD@@@Z` | `0x63B0` | 395 | UnwindData |  |
| 100 | `?GetLanguage@CNewOS@@SAPEBGPEAU_BLACKBOARD@@@Z` | `0x6550` | 395 | UnwindData |  |
| 101 | `?GetNewOSDetails@CNewOS@@AEAAXXZ` | `0x66F0` | 460 | UnwindData |  |
| 102 | `?GetNewOSVersionInformation@CNewOS@@QEAAXPEAG@Z` | `0x68D0` | 60 | UnwindData |  |
| 117 | `?GetWinImageArch@CNewOS@@SAKPEAU_BLACKBOARD@@@Z` | `0x6920` | 40 | UnwindData |  |
| 6 | `??0CInstallSource@@QEAA@PEAU_BLACKBOARD@@@Z` | `0x6950` | 386 | UnwindData |  |
| 72 | `?DetermineInstallImageType@CInstallSource@@SAKPEAU_BLACKBOARD@@@Z` | `0x6B70` | 58 | UnwindData |  |
| 73 | `?DetermineInstallMedia@CInstallSource@@SAKPEAU_BLACKBOARD@@@Z` | `0x6BB0` | 173 | UnwindData |  |
| 74 | `?DetermineInstallMediaHashLabel@CInstallSource@@SAKPEAU_BLACKBOARD@@@Z` | `0x6C70` | 618 | UnwindData |  |
| 75 | `?DetermineInstallType@CInstallSource@@SAKPEAU_BLACKBOARD@@@Z` | `0x6EE0` | 88 | UnwindData |  |
| 92 | `?GetDeviceDword@CInstallSource@@QEAAKW4eDeviceDword@1@@Z` | `0x6F40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?IsInternal@CInstallSource@@AEAAHXZ` | `0x6F90` | 1,200 | UnwindData |  |
| 11 | `??0CSqmDiagConsumer@@QEAA@XZ` | `0x7580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??1CSqmDiagConsumer@@UEAA@XZ` | `0x75B0` | 50 | UnwindData |  |
| 58 | `?AddToStream@CSqmDiagConsumer@@UEAAKKKK@Z` | `0x75F0` | 360 | UnwindData |  |
| 59 | `?AddToStream@CSqmDiagConsumer@@UEAAKKKPEAG@Z` | `0x7760` | 360 | UnwindData |  |
| 68 | `?CreateInstance@CDiagConsumerAdaptorFactory@@SAKPEAPEAVIDiagConsumer@@@Z` | `0x78D0` | 446 | UnwindData |  |
| 69 | `?DeleteInstance@CDiagConsumerAdaptorFactory@@SAXPEAVIDiagConsumer@@@Z` | `0x7AA0` | 31 | UnwindData |  |
| 79 | `?DoneReporting@CSqmDiagConsumer@@UEAAKPEAGK@Z` | `0x7AD0` | 2,125 | UnwindData |  |
| 118 | `?InLHPlus@CSqmDiagConsumer@@CAHXZ` | `0x8330` | 122 | UnwindData |  |
| 120 | `?Initialize@CSqmDiagConsumer@@QEAAKKPEAU_GUID@@PEAG1HK@Z` | `0x83B0` | 1,237 | UnwindData |  |
| 121 | `?Initialize@CSqmDiagConsumer@@UEAAKKPEAU_GUID@@@Z` | `0x8890` | 1,213 | UnwindData |  |
| 127 | `?IsSubmitSuccessful@CSqmDiagConsumer@@UEAAHPEAG@Z` | `0x8D60` | 390 | UnwindData |  |
| 149 | `?ProcessFailedUpload@CSqmDiagConsumer@@CAKPEAG@Z` | `0x8EF0` | 631 | UnwindData |  |
| 152 | `?Set@CSqmDiagConsumer@@UEAAKKK@Z` | `0x9170` | 353 | UnwindData |  |
| 153 | `?Set@CSqmDiagConsumer@@UEAAKKPEAG@Z` | `0x92E0` | 353 | UnwindData |  |
| 156 | `?Shutdown@CSqmDiagConsumer@@UEAAKXZ` | `0x9450` | 178 | UnwindData |  |
| 157 | `?SqmUploadCallBack@CSqmDiagConsumer@@CAHJPEBGK@Z` | `0x96F0` | 785 | UnwindData |  |
| 159 | `?Submit@CSqmDiagConsumer@@UEAAKPEAGH@Z` | `0x9AB0` | 1,048 | UnwindData |  |
| 15 | `??0InstallData@@QEAA@PEAU_BLACKBOARD@@@Z` | `0x9ED0` | 89 | UnwindData |  |
| 17 | `??0MachineHardWare@@QEAA@XZ` | `0x9F30` | 73 | UnwindData |  |
| 19 | `??0NewSystem@@QEAA@PEAU_BLACKBOARD@@@Z` | `0x9F80` | 89 | UnwindData |  |
| 21 | `??0OldSystem@@QEAA@XZ` | `0x9FE0` | 73 | UnwindData |  |
| 31 | `??1InstallData@@QEAA@XZ` | `0xA030` | 41 | UnwindData |  |
| 32 | `??1MachineHardWare@@QEAA@XZ` | `0xA060` | 45 | UnwindData |  |
| 33 | `??1NewSystem@@QEAA@XZ` | `0xA0A0` | 41 | UnwindData |  |
| 34 | `??1OldSystem@@QEAA@XZ` | `0xA0D0` | 55 | UnwindData |  |
| 122 | `?IsAlreadyProcessed@InstallData@@UEAAHPEAU_BLACKBOARD@@@Z` | `0xA110` | 107 | UnwindData |  |
| 123 | `?IsAlreadyProcessed@MachineHardWare@@UEAAHPEAU_BLACKBOARD@@@Z` | `0xA190` | 107 | UnwindData |  |
| 124 | `?IsAlreadyProcessed@NewSystem@@UEAAHPEAU_BLACKBOARD@@@Z` | `0xA210` | 107 | UnwindData |  |
| 125 | `?IsAlreadyProcessed@OldSystem@@UEAAHPEAU_BLACKBOARD@@@Z` | `0xA290` | 107 | UnwindData |  |
| 132 | `?LogToBB@InstallData@@UEAAXPEAU_BLACKBOARD@@@Z` | `0xA310` | 707 | UnwindData |  |
| 133 | `?LogToBB@MachineHardWare@@UEAAXPEAU_BLACKBOARD@@@Z` | `0xA5E0` | 517 | UnwindData |  |
| 134 | `?LogToBB@NewSystem@@UEAAXPEAU_BLACKBOARD@@@Z` | `0xA7F0` | 644 | UnwindData |  |
| 135 | `?LogToBB@OldSystem@@UEAAXPEAU_BLACKBOARD@@@Z` | `0xAA80` | 953 | UnwindData |  |
| 137 | `?LogToFile@MachineHardWare@@UEAAXXZ` | `0xAE40` | 394 | UnwindData |  |
| 60 | `CallBack_DiagnosticDataGeneration` | `0xB200` | 3,607 | UnwindData |  |
| 61 | `CallBack_DiagnosticDataSend` | `0xC020` | 2,143 | UnwindData |  |
| 62 | `CallBack_EditionID` | `0xC890` | 3,558 | UnwindData |  |
| 63 | `CallBack_RestartSetup` | `0xD680` | 910 | UnwindData |  |
| 64 | `Callback_Diagnostic_Unattend` | `0xDA20` | 1,188 | UnwindData |  |
| 65 | `CollectAndSendDiagDataToSQM` | `0xDEF0` | 2,941 | UnwindData |  |
| 66 | `CollectAndSendDiagDataToWatson` | `0xEA80` | 2,132 | UnwindData |  |
| 76 | `DiagnosticDataSendWorker` | `0xF690` | 3,474 | UnwindData |  |
| 78 | `DoWatsonReporting` | `0x10430` | 1,174 | UnwindData |  |
| 142 | `Module_Init_Diagnostic` | `0x11450` | 1,284 | UnwindData |  |
| 145 | `ObtainBucketingParamsFromBlackBoard` | `0x119A0` | 1,648 | UnwindData |  |
| 146 | `ObtainBucketingParamsFromLogFile` | `0x12020` | 3,885 | UnwindData |  |
| 147 | `ObtainFilesToAttach` | `0x12F60` | 637 | UnwindData |  |
| 148 | `ProcessDiagnosticDetails` | `0x13230` | 383 | UnwindData |  |
| 151 | `RestoreIniValues` | `0x13500` | 1,221 | UnwindData |  |
| 154 | `SetFromBlackBoard` | `0x14170` | 856 | UnwindData |  |
| 155 | `SetFromFile` | `0x14680` | 1,977 | UnwindData |  |
| 158 | `StartNetworking` | `0x157D0` | 2,087 | UnwindData |  |
| 3 | `??0CCountArray@@QEAA@XZ` | `0x162C0` | 58 | UnwindData |  |
| 23 | `??1CCountArray@@QEAA@XZ` | `0x16300` | 173 | UnwindData |  |
| 99 | `?GetInfo@CCountArray@@QEAAHIAEAK000AEAPEAG@Z` | `0x163C0` | 96 | UnwindData |  |
| 119 | `?IncrementCount@CCountArray@@QEAAHKKKPEBG@Z` | `0x16430` | 434 | UnwindData |  |
| 143 | `?NewElement@CCountArray@@AEAAHKKKPEBG@Z` | `0x165F0` | 568 | UnwindData |  |
| 50 | `??_7CAccessWMI@@6B@` | `0x1EB28` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??_7CMoboAndProcInfo@@6B@` | `0x1EB30` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??_7InstallData@@6B@` | `0x1EC20` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??_7OldSystem@@6B@` | `0x1EC38` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??_7NewSystem@@6B@` | `0x1EC50` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??_7MachineHardWare@@6B@` | `0x1EC68` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??_7CSqmDiagConsumer@@6B@` | `0x1EC80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??_7IDiagConsumer@@6B@` | `0x1ECD0` | 11,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?MAX_CHAR_SIZE@CExistingOS@@0HB` | `0x21A60` | 50,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?MAX_CHAR_SIZE@CNewOS@@0HB` | `0x21A60` | 50,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `g_Sqm` | `0x2E028` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `g_Kernel32` | `0x2E038` | 296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `g_Shell32` | `0x2E160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `g_Wdscore` | `0x2E170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `g_DiagERApi` | `0x2E180` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?m_szLanguage@CNewOS@@0PAGA` | `0x2EAE0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?m_szEdition@CNewOS@@0PAGA` | `0x2EBE0` | 0 | Indeterminate |  |
