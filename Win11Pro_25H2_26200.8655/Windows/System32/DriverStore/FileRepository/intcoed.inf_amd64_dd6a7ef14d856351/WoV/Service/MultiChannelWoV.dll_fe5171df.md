# Binary Specification: MultiChannelWoV.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\intcoed.inf_amd64_dd6a7ef14d856351\WoV\Service\MultiChannelWoV.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe5171df6c2a62012d76ebd9150e858eba0d6fffbad211ebeb7998838b12642a`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `?ReleaseSpeakerModelCreatorInstance@MultiChannelWovEnrollment@@YAXPEAVISpeakerModelCreator@1@@Z` | `0x11D0` | 19,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `?GetApiVersion@MultichannelWov@@YAPEBDXZ` | `0x5C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MultiChannelWovGetApiVersion` | `0x5C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?GetBuildVersion@MultichannelWov@@YAPEBDXZ` | `0x5C40` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MultiChannelWovGetBuildVersion` | `0x5C40` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MultiChannelWovSetKpDetectedCallback` | `0x5F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MultiChannelWovSetKpSegmentsDetectedCallback` | `0x5FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MultiChannelWovCreateInstance` | `0x5FC0` | 587 | UnwindData |  |
| 14 | `MultiChannelWovReleaseInstance` | `0x6210` | 35 | UnwindData |  |
| 10 | `MultiChannelWovFeed` | `0x6510` | 127 | UnwindData |  |
| 11 | `MultiChannelWovFlush` | `0x6590` | 113 | UnwindData |  |
| 15 | `MultiChannelWovReset` | `0x6610` | 83 | UnwindData |  |
| 3 | `?GetInstance@MultichannelWovVerification@@YA?AW4EMultiChannelWovStatusCode@@PEBVIMultiChannelWoVConfig@@PEAVIMultiChannelWoVLogger@@AEAPEAVIMultiChannelWoV@@@Z` | `0x7450` | 321 | UnwindData |  |
| 6 | `?ReleaseInstance@MultichannelWovVerification@@YAXPEAVIMultiChannelWoV@@@Z` | `0x75A0` | 16 | UnwindData |  |
| 5 | `?GetUtteranceCollectorInstance@MultiChannelWovEnrollment@@YA?AW4EMultiChannelWovStatusCode@@PEBVIUtteranceCollectorConfig@1@PEAVIMultiChannelWoVLogger@@PEAVIUtteranceCollectorEventHandler@1@AEAPEAVIUtteranceCollector@1@@Z` | `0x75E0` | 413 | UnwindData |  |
| 8 | `?ReleaseUtteranceCollectorInstance@MultiChannelWovEnrollment@@YAXPEAVIUtteranceCollector@1@@Z` | `0x7780` | 16 | UnwindData |  |
| 4 | `?GetSpeakerModelCreatortInstance@MultiChannelWovEnrollment@@YA?AW4EMultiChannelWovStatusCode@@PEBVISpeakerModelCreatorConfig@1@PEAVIMultiChannelWoVLogger@@AEAPEAVISpeakerModelCreator@1@@Z` | `0x77C0` | 377,858 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
