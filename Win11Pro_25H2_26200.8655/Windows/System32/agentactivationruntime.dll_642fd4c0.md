# Binary Specification: agentactivationruntime.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\agentactivationruntime.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `642fd4c04da07ffe15d3122d48bcb7c9e22149e02dbb859fe480a8a359e862f3`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `?CreateAgentActivationRuntime@@YA?AV?$shared_ptr@VIAgentActivationRuntime@VoiceAgentServices@Microsoft@@@std@@XZ` | `0x1D870` | 213 | UnwindData |  |
| 2 | `?GetAgentActivationRuntime@@YA?AV?$shared_ptr@VIAgentActivationRuntime@VoiceAgentServices@Microsoft@@@std@@XZ` | `0x301A0` | 242 | UnwindData |  |
| 3 | `?GetLoggerInstance@@YAAEAVLogger@VoiceAgentServices@Microsoft@@XZ` | `0x41660` | 10,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?ReleaseAgentActivationRuntime@@YAXXZ` | `0x43FE0` | 72 | UnwindData |  |
