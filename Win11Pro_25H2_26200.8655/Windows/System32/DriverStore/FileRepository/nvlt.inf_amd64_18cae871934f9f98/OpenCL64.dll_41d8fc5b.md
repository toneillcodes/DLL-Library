# Binary Specification: OpenCL64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\OpenCL64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `41d8fc5b4f3c056c8e78d254f073480ebfb53bfd477a6deff9feffbc0ac935c9`
* **Total Exported Functions:** 123

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 85 | `clGetPlatformIDs` | `0x20E0` | 216 | UnwindData |  |
| 73 | `clGetExtensionFunctionAddress` | `0x2320` | 180 | UnwindData |  |
| 74 | `clGetExtensionFunctionAddressForPlatform` | `0x2480` | 83 | UnwindData |  |
| 86 | `clGetPlatformInfo` | `0x24E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `clGetDeviceIDs` | `0x24F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `clGetDeviceInfo` | `0x2500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `clCreateContext` | `0x2510` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `clCreateContextFromType` | `0x2560` | 173 | UnwindData |  |
| 101 | `clRetainContext` | `0x2610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `clReleaseContext` | `0x2620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `clGetContextInfo` | `0x2630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `clRetainCommandQueue` | `0x2640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `clReleaseCommandQueue` | `0x2650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `clGetCommandQueueInfo` | `0x2660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `clCreateBuffer` | `0x2670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `clRetainMemObject` | `0x26A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `clReleaseMemObject` | `0x26C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `clGetSupportedImageFormats` | `0x26E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `clGetMemObjectInfo` | `0x2700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `clGetImageInfo` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `clRetainSampler` | `0x2740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `clReleaseSampler` | `0x2760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `clGetSamplerInfo` | `0x2780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `clCreateProgramWithSource` | `0x27A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `clCreateProgramWithBinary` | `0x27D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `clRetainProgram` | `0x2800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `clReleaseProgram` | `0x2820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `clBuildProgram` | `0x2840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `clGetProgramInfo` | `0x2860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `clGetProgramBuildInfo` | `0x2880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `clCreateKernel` | `0x28A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `clCreateKernelsInProgram` | `0x28C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `clRetainKernel` | `0x28E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `clReleaseKernel` | `0x2900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `clSetKernelArg` | `0x2920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `clGetKernelInfo` | `0x2940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `clGetKernelWorkGroupInfo` | `0x2960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `clWaitForEvents` | `0x2980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `clGetEventInfo` | `0x29B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `clRetainEvent` | `0x29D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `clReleaseEvent` | `0x29F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `clGetEventProfilingInfo` | `0x2A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `clFlush` | `0x2A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `clFinish` | `0x2A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `clEnqueueReadBuffer` | `0x2A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `clEnqueueWriteBuffer` | `0x2A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `clEnqueueCopyBuffer` | `0x2AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `clEnqueueReadImage` | `0x2AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `clEnqueueWriteImage` | `0x2AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `clEnqueueCopyImage` | `0x2B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `clEnqueueCopyImageToBuffer` | `0x2B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `clEnqueueCopyBufferToImage` | `0x2B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `clEnqueueMapBuffer` | `0x2B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `clEnqueueMapImage` | `0x2BA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `clEnqueueUnmapMemObject` | `0x2BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `clEnqueueNDRangeKernel` | `0x2BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `clEnqueueNativeKernel` | `0x2C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `clSetCommandQueueProperty` | `0x2C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `clCreateImage2D` | `0x2C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `clCreateImage3D` | `0x2C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `clEnqueueMarker` | `0x2CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `clEnqueueWaitForEvents` | `0x2CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `clEnqueueBarrier` | `0x2CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `clUnloadCompiler` | `0x2D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `clCreateCommandQueue` | `0x2D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `clCreateSampler` | `0x2D30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `clEnqueueTask` | `0x2D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `clCreateSubBuffer` | `0x2D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `clSetMemObjectDestructorCallback` | `0x2DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `clCreateUserEvent` | `0x2DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `clSetUserEventStatus` | `0x2DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `clSetEventCallback` | `0x2E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `clEnqueueReadBufferRect` | `0x2E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `clEnqueueWriteBufferRect` | `0x2E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `clEnqueueCopyBufferRect` | `0x2E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `clCreateSubDevices` | `0x2E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `clRetainDevice` | `0x2EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `clReleaseDevice` | `0x2ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `clCreateImage` | `0x2EF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `clCreateProgramWithBuiltInKernels` | `0x2F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `clCompileProgram` | `0x2F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `clLinkProgram` | `0x2F70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `clUnloadPlatformCompiler` | `0x2FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `clGetKernelArgInfo` | `0x2FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `clEnqueueFillBuffer` | `0x2FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `clEnqueueFillImage` | `0x3000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `clEnqueueMigrateMemObjects` | `0x3020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `clEnqueueMarkerWithWaitList` | `0x3040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `clEnqueueBarrierWithWaitList` | `0x3060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `clCreateCommandQueueWithProperties` | `0x3080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `clCreatePipe` | `0x30A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `clGetPipeInfo` | `0x30D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `clSVMAlloc` | `0x30F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `clSVMFree` | `0x3110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `clCreateSamplerWithProperties` | `0x3120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `clSetKernelArgSVMPointer` | `0x3140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `clSetKernelExecInfo` | `0x3160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `clEnqueueSVMFree` | `0x3180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `clEnqueueSVMMemcpy` | `0x31A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `clEnqueueSVMMemFill` | `0x31C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `clEnqueueSVMMap` | `0x31E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `clEnqueueSVMUnmap` | `0x3200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `clSetDefaultDeviceCommandQueue` | `0x3220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `clGetDeviceAndHostTimer` | `0x3240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `clGetHostTimer` | `0x3260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `clCreateProgramWithIL` | `0x3280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `clCloneKernel` | `0x32A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `clGetKernelSubGroupInfo` | `0x32C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `clEnqueueSVMMigrateMem` | `0x32E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `clSetProgramSpecializationConstant` | `0x3300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `clSetProgramReleaseCallback` | `0x3320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `clSetContextDestructorCallback` | `0x3340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `clCreateBufferWithProperties` | `0x3360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `clCreateImageWithProperties` | `0x3390` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `clCreateFromGLBuffer` | `0x3780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `clCreateFromGLTexture` | `0x37A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `clCreateFromGLRenderbuffer` | `0x37D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `clGetGLObjectInfo` | `0x37F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `clGetGLTextureInfo` | `0x3810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `clEnqueueAcquireGLObjects` | `0x3830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `clEnqueueReleaseGLObjects` | `0x3850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `clCreateFromGLTexture2D` | `0x3870` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `clCreateFromGLTexture3D` | `0x38A0` | 607,636 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
