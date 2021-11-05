from conans import ConanFile, tools, CMake


class MQTTcppConan(ConanFile):
    name = "mqtt_cpp"
    homepage = "https://github.com/redboltz/mqtt_cpp"
    license = "BSL-1.0"
    version = "12.0.0"
    scm = {
        "type" : "git",
        "url" : "https://github.com/redboltz/mqtt_cpp",
        "revision" : "v%s" % version
        }

    requires = ("boost/1.76.0", "openssl/1.1.1l")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["MQTT_BUILD_TESTS"] = False
        cmake.definitions["MQTT_BUILD_EXAMPLES"] = False
        cmake.configure()
        cmake.build()
        cmake.install()
        cmake.patch_config_paths()

    def package_info(self):
        self.cpp_info.builddirs.append("lib/cmake")
        
    def package_id(self):
        self.info.header_only()
    
        
    
